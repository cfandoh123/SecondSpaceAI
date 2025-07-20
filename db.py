import sqlite3

DB_PATH = "interests.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def save_interests(user_id, interests):
    """
    Save user interests to the database (mocked).
    """
    pass  # Mocked: do nothing

def get_all_interests():
    """
    Return a mock list of user interests.
    """
    return [
        ("U123", "hiking, AI, music"),
        ("U456", "AI, music, photography"),
        ("U789", "cooking, running, jazz")
    ]

def find_similar_users(user_id, interests):
    """
    Simulate finding users with similar interests.
    """
    # Mock: return users with at least one shared interest
    all_users = get_all_interests()
    user_interests = set([i.strip() for i in interests.split(",")])
    matches = []
    for uid, ints in all_users:
        if uid == user_id:
            continue
        other_interests = set([i.strip() for i in ints.split(",")])
        if user_interests & other_interests:
            matches.append((uid, ints))
    return matches

def save_oauth_token(user_id, token):
    """
    Simulate saving a user's OAuth token.
    """
    pass  # Mocked: do nothing 