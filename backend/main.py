# backend/main.py
import os
from fastapi import FastAPI
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

# Scopes: the permissions we request from the user
SCOPES = "user-read-private user-read-email user-top-read user-read-recently-played"

@app.get("/")
def read_root():
    # Redirect the root to our login page for simplicity
    return RedirectResponse(url="/login")

@app.get("/login")
def login():
    """
    This endpoint builds the Spotify authorization URL and redirects the user to it.
    """
    # Build the URL with all the required parameters
    auth_url_with_params = (
        f"{AUTH_URL}?client_id={CLIENT_ID}"
        f"&response_type=code"
        f"&redirect_uri={REDIRECT_URI}"
        f"&scope={SCOPES}"
        f"&show_dialog=true"
    )
    
    # Use RedirectResponse to send the user's browser to the Spotify login page
    return RedirectResponse(url=auth_url_with_params)

# The /callback endpoint will be added in the next step
