import requests
import json
# ----------------------
# PASTE VARIABLES BELOW
# ----------------------

# Paste your Spotify API access token below in quotes
SpotifyAPIToken = "ENTER YOUR TOKEN HERE"
# Paste your Airtable URL below in quotes
airtable_url = "https://api.airtable.com/v0/{YOUR BASE ID HERE}/Music"
# Paste your Airtable API key below in quotes
AirtableAPIKey = "YOUR KEY HERE"


# ------
# CODE
# ------
airtable_headers = {
    "Accept" : "aplication/json",
    "Content-Type" : "application/json",
    "Authorization" : "Bearer {token}".format(token=AirtableAPIKey)
}

if __name__ == "__main__":
    headers = {
        "Accept" : "aplication/json",
        "Content-Type" : "application/json",
        "Authorization" : "Bearer {token}".format(token=SpotifyAPIToken)
    }
    
    r = requests.get("https://api.spotify.com/v1/me/tracks?next",headers=headers)
    
    data = r.json()
    track_ids = []
    song_names = []
    artist_names = []
    dates_added = []
    album_images = []
    release_dates = []
    
    # get first batch of songs
    for song in data["items"]:
        track_ids.append(song["track"]["id"])
        song_names.append(song["track"]["name"])
        artist_names.append(song["track"]["artists"][0]["name"])
        dates_added.append(song["added_at"])
        album_images.append(song["track"]["album"]["images"][0]["url"])
        release_dates.append(song["track"]["album"]["release_date"])
        #format Airtable request
        body = json.dumps({
        "fields": {
            "Track ID": song["track"]["id"],
            "Song Name": song["track"]["name"],
            "Date Added": song["added_at"],
            "Album Image": [
                {
                    "url": song["track"]["album"]["images"][0]["url"]
                }
            ],
            "Release Date": song["track"]["album"]["release_date"],
            "Artist": song["track"]["artists"][0]["name"]
        }
        })
        f = requests.post(airtable_url,headers=airtable_headers, data=body)
    # get the rest of the songs
    while data["next"]:
        r = requests.get(data["next"],headers=headers)
        data = r.json()
        for song in data["items"]:
            track_ids.append(song["track"]["id"])
            song_names.append(song["track"]["name"])
            artist_names.append(song["track"]["artists"][0]["name"])
            dates_added.append(song["added_at"])
            album_images.append(song["track"]["album"]["images"][0]["url"])
            release_dates.append(song["track"]["album"]["release_date"])
            body = json.dumps({
            "fields": {
                "Track ID": song["track"]["id"],
                "Song Name": song["track"]["name"],
                "Date Added": song["added_at"],
                "Album Image": [
                    {
                        "url": song["track"]["album"]["images"][0]["url"]
                    }
                ],
                "Release Date": song["track"]["album"]["release_date"],
                "Artist": song["track"]["artists"][0]["name"]
            }
            })
            f = requests.post(airtable_url,headers=airtable_headers, data=body)
