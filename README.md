# Spotify + Airtable
Copies Liked Song information into Airtable
## Set Up
### Create New Table in Airtable
Create a new table named "Music" in an existing Airtable Base with the following columns:
| Column      | Type        |
| ----------- | ----------- |
| Song Name   | Text        |
| Artist      | Text        |
| Track ID    | Text        |
| Release Date| Date        |
| Album Image | Attachment  |
| Date Added  | DateTime    |

### Get your Airtable API URL
Go to `https://airtable.com/api` and select the base you created your table in. Click on "Music Table" then, "List Records". You'll see in the example code a url that looks like this: `https://api.airtable.com/v0/appx{SOMETEXT}/Music`. Copy and paste that into the variable called "airtable_url" in main.py.

### Get Your Airtable API Key
Go to `https://airtable.com/account` and click on generate API Key. Paste this key in the variable AirtableAPIKey in main.py

### Get Your Spotify API Token
Go to `https://developer.spotify.com/dashboard/applications` and create a Spotify Developer Account. Then go to `https://developer.spotify.com/console/get-current-user-saved-tracks/` and click "Get Token". Copy that code and paste it in the variable "SpotifyAPIToken" in main.py.
