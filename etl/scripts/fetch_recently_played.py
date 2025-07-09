# etl/scripts/fetch_recently_played.py
import os
import requests
import base64
import json
from dotenv import load_dotenv

def get_access_token(client_id, client_secret, refresh_token):
    """
    Gets a new access token from Spotify using the refresh token.
    """
    # Spotify's endpoint for refreshing tokens
    TOKEN_URL = "https://accounts.spotify.com/api/token"

    # Prepare the authentication header (Client ID:Client Secret encoded in Base64)
    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")
    
    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    
    # Prepare the request payload
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
    }

    # Make the POST request to get a new access token
    response = requests.post(TOKEN_URL, headers=headers, data=data)

    if response.status_code != 200:
        print(f"Error refreshing token: {response.json()}")
        return None

    # Extract the new access token from the response
    new_access_token = response.json().get("access_token")
    return new_access_token

def fetch_recently_played(access_token):
    """
    Fetches the user's recently played tracks using the access token.
    """
    # Spotify's endpoint for recently played tracks
    RECENTLY_PLAYED_URL = "https://api.spotify.com/v1/me/player/recently-played"
    
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    
    # We can limit the number of items we get back. Max is 50.
    params = {
        "limit": 50
    }

    response = requests.get(RECENTLY_PLAYED_URL, headers=headers, params=params)

    if response.status_code != 200:
        print(f"Error fetching recently played: {response.json()}")
        return None

    return response.json()

def main():
    """
    Main function to orchestrate the script.
    """
    # --- Configuration ---
    # We need to load the .env file from the backend directory.
    # This is a temporary solution for local testing.
    # In AWS Lambda, we will use environment variables directly.
    dotenv_path = os.path.join(os.path.dirname(__file__), '../../backend/.env')
    load_dotenv(dotenv_path=dotenv_path)

    CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
    CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
    REFRESH_TOKEN = os.getenv("SPOTIFY_REFRESH_TOKEN")

    if not all([CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN]):
        print("Error: Ensure SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, and SPOTIFY_REFRESH_TOKEN are set in backend/.env")
        return

    print("--- Step 1: Refreshing Access Token ---")
    access_token = get_access_token(CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN)

    if not access_token:
        print("Could not get access token. Exiting.")
        return
    
    print("Access Token successfully refreshed!")

    print("\n--- Step 2: Fetching Recently Played Tracks ---")
    recently_played_data = fetch_recently_played(access_token)
    
    if not recently_played_data:
        print("Could not fetch recently played tracks. Exiting.")
        return

    # Pretty-print the JSON data to the console
    print(json.dumps(recently_played_data, indent=4))
    print("\nSuccessfully fetched recently played tracks!")


if __name__ == "__main__":
    main()
