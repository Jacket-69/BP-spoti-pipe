# backend/main.py
import os
import requests
import base64
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Get credentials securely from environment variables
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = "http://127.0.0.1:8000/callback"

# Spotify API URLs
AUTH_URL = "https://accounts.spotify.com/authorize"
TOKEN_URL = "https://accounts.spotify.com/api/token"

# Scopes: the permissions we request from the user
SCOPES = "user-read-private user-read-email user-top-read user-read-recently-played"

@app.get("/")
def read_root():
    # Redirect the root to our login page for simplicity
    return RedirectResponse(url="/login")

@app.get("/login")
def login():
    """
    Builds the Spotify authorization URL and redirects the user to it.
    """
    auth_url_with_params = (
        f"{AUTH_URL}?client_id={CLIENT_ID}"
        f"&response_type=code"
        f"&redirect_uri={REDIRECT_URI}"
        f"&scope={SCOPES}"
        f"&show_dialog=true"
    )
    return RedirectResponse(url=auth_url_with_params)


@app.get("/callback")
def callback(request: Request):
    """
    Handles the redirect from Spotify after user authorization.
    Exchanges the authorization code for an access token.
    """
    # 1. Extract the authorization code from the request URL's query parameters.
    # 'request: Request' is a FastAPI dependency that gives us access to the incoming request.
    try:
        code = request.query_params["code"]
    except KeyError:
        return {"error": "Authorization code not found in callback."}

    # 2. Prepare the payload for the POST request to get the token.
    token_data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
    }

    # 3. Prepare the headers. Spotify requires our app's credentials
    # to be sent in the 'Authorization' header, encoded in Base64.
    auth_string = f"{CLIENT_ID}:{CLIENT_SECRET}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    # 4. Make the POST request to Spotify's token endpoint.
    response = requests.post(TOKEN_URL, data=token_data, headers=headers)

    # 5. Check if the request was successful and return the token data.
    if response.status_code == 200:
        # In the future, we will securely store these tokens.
        # For now, we just display them to confirm success.
        return response.json()
    else:
        # If there was an error, show it for debugging.
        return {"error": "Failed to retrieve access token", "details": response.json()}
