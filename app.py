import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
from flask import Flask, request
# Mocked helpers
import db
import calendar_integration

# Load environment variables from .env file
load_dotenv()

SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SLACK_SIGNING_SECRET = os.environ.get("SLACK_SIGNING_SECRET")

app = App(token=SLACK_BOT_TOKEN, signing_secret=SLACK_SIGNING_SECRET)
flask_app = Flask(__name__)
handler = SlackRequestHandler(app)

# --- Workflow ---
# 1. User sets interests with /interests
# 2. User runs /find_match to find similar users
# 3. Bot suggests matches and offers to schedule a meeting
# 4. Bot simulates Google OAuth and calendar scheduling

@app.command("/interests")
def handle_interests(ack, body, respond):
    ack()
    user_id = body["user_id"]
    text = body.get("text", "")
    if not text:
        respond("Please provide your interests, e.g. `/interests hiking, AI, music`.")
        return
    db.save_interests(user_id, text)
    respond(f"Your interests have been saved: {text}")

@app.command("/find_match")
def handle_find_match(ack, body, respond):
    ack()
    user_id = body["user_id"]
    # For demo, use the text as interests
    text = body.get("text", "")
    if not text:
        respond("Please provide your interests, e.g. `/find_match hiking, AI, music`.")
        return
    matches = db.find_similar_users(user_id, text)
    if not matches:
        respond("No similar users found right now. Try again later!")
        return
    match = matches[0]
    respond(f"Found a match: <@{match[0]}> with interests: {match[1]}\nWould you like to schedule a coffee chat?")
    # Simulate calendar integration
    oauth_url = calendar_integration.start_google_oauth(user_id)
    respond(f"To schedule, please connect your Google Calendar: {oauth_url}")
    # Simulate fetching free times and scheduling
    free_times = calendar_integration.fetch_free_times("user@example.com")
    event = calendar_integration.schedule_meeting("user1@example.com", "user2@example.com", free_times[0])
    respond(f"Meeting scheduled! Event link: {event['event_link']}")

@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)

if __name__ == "__main__":
    flask_app.run(port=3000) 