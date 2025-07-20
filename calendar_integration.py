# calendar_integration.py

def start_google_oauth(user_id):
    """
    Simulate starting the Google OAuth flow for a user.
    In production, this would redirect the user to Google's OAuth consent screen.
    """
    return f"https://mock-oauth-url.com/auth?user_id={user_id}"

def fetch_free_times(user_email):
    """
    Simulate fetching free times from a user's Google Calendar.
    In production, this would use the Google Calendar API to get free/busy slots.
    """
    return ["2024-06-10T10:00:00Z", "2024-06-10T15:00:00Z"]

def schedule_meeting(user1_email, user2_email, time):
    """
    Simulate scheduling a meeting between two users.
    In production, this would create a calendar event via the Google Calendar API.
    """
    return {
        "status": "success",
        "event_link": f"https://calendar.google.com/event?eid=mockevent{time}"
    } 