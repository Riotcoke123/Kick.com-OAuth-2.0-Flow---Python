import requests
import urllib.parse

# OAuth2 Client Credentials
CLIENT_ID = ""
CLIENT_SECRET = ""
REDIRECT_URI = "http://localhost:8000/callback"  # Change to your registered redirect URI
AUTH_URL = "https://kick.com/oauth2/authorize"
TOKEN_URL = "https://kick.com/oauth2/token"

# Step 1: Redirect user to Kick's OAuth2 authorization page
def get_authorization_url():
    params = {
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
        "scope": "user_read",  # Adjust scope as needed
    }
    url = f"{AUTH_URL}?{urllib.parse.urlencode(params)}"
    print("Visit this URL to authorize:")
    print(url)

# Step 2: Exchange authorization code for access token
def get_tokens(auth_code):
    data = {
        "grant_type": "authorization_code",
        "code": auth_code,
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }

    response = requests.post(TOKEN_URL, data=data)
    if response.status_code == 200:
        tokens = response.json()
        print("Access Token:", tokens["access_token"])
        print("Refresh Token:", tokens.get("refresh_token"))
    else:
        print("Failed to get tokens:")
        print(response.status_code, response.text)

# Run the flow
if __name__ == "__main__":
    get_authorization_url()
    # After visiting the URL, paste the code you get back
    code = input("Paste the authorization code here: ")
    get_tokens(code)
