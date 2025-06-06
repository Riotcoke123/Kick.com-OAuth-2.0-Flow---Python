import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN_FILE = "tokens.json"
AUTH_URL = "https://kick.com/oauth2/authorize"
TOKEN_URL = "https://kick.com/oauth2/token"

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

def save_tokens(data):
    with open(TOKEN_FILE, "w") as f:
        json.dump(data, f)

def load_tokens():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r") as f:
            return json.load(f)
    return {}

def get_authorization_url():
    from urllib.parse import urlencode
    params = {
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
        "scope": "user_read"
    }
    return f"{AUTH_URL}?{urlencode(params)}"

def exchange_code_for_tokens(code):
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }
    response = requests.post(TOKEN_URL, data=data)
    response.raise_for_status()
    tokens = response.json()
    save_tokens(tokens)
    return tokens

def refresh_tokens():
    tokens = load_tokens()
    refresh_token = tokens.get("refresh_token")
    if not refresh_token:
        print("No refresh token found.")
        return

    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }
    response = requests.post(TOKEN_URL, data=data)
    if response.status_code == 200:
        new_tokens = response.json()
        save_tokens(new_tokens)
        print("✅ Tokens refreshed successfully.")
    else:
        print("❌ Token refresh failed:", response.text)
