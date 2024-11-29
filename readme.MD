# Billboard Hot 100 to Spotify Playlist

This Python script allows you to automatically create a Spotify playlist based on the **Billboard Hot 100** chart for any given date. By scraping the chart data and searching for the songs on Spotify, it adds them to a new private playlist on your account.

## Features

- **Billboard Hot 100 Scraping**: Fetches the Billboard Hot 100 chart for a specific date.
- **Spotify Playlist Creation**: Automatically creates a private Spotify playlist.
- **Track Search & Add**: Searches for each song on Spotify and adds it to the playlist.

## Requirements

- Python 3.x
- [requests](https://pypi.org/project/requests/) — for web scraping the Billboard chart.
- [spotipy](https://pypi.org/project/spotipy/) — for interacting with the Spotify API.
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/) — for parsing the Billboard chart HTML.
- A **Spotify Developer Account** to get your API credentials.


## Setup

### 1. **Create a Spotify Developer Account**

- Visit [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) and log in.
- Create a new app to get your `client_id`, `client_secret`, and `redirect_uri`.

### 2. **Set Environment Variables**

To securely use your Spotify credentials, create a `.env` file in your project directory or set the following environment variables:

```bash
client_id=<your_spotify_client_id>
client_secret=<your_spotify_client_secret>
username=<your_spotify_username>
redirect_uri=<your_spotify_redirect_uri>
```

Alternatively, you can directly edit the values within the script, though using environment variables is recommended for security.

## How to Use

### 1. **Clone the Repository**

Download or clone the script to your local machine.

### 2. **Set Your Credentials**

Ensure that your Spotify credentials (client ID, client secret, username, and redirect URI) are set in your environment variables or directly in the script.

### 3. **Run the Script**

Execute the script in your terminal:

```bash
python create_spotify_playlist.py
```

### 4. **Input the Date**

When prompted, enter a date in the format `YYYY-MM-DD` to fetch the Billboard Hot 100 chart for that date.

For example:
```
2022-01-01
```

### 5. **Playlist Creation**

- The script will:
  - Scrape the Billboard Hot 100 chart for the given date.
  - Search for the top 100 songs on Spotify.
  - Create a new **private** playlist on your Spotify account.
  - Add the found tracks to the playlist.

Once completed, you’ll have a Spotify playlist with the songs from the Billboard Hot 100 chart for the specified date!

## How It Works

1. **Scraping the Billboard Chart**: The script uses `requests` and `BeautifulSoup` to scrape the song names from the Billboard Hot 100 page for the given date.
2. **Spotify Authentication**: The script authenticates with the Spotify API using the `spotipy` library with OAuth2, allowing it to create playlists and add tracks on your behalf.
3. **Searching for Songs**: It searches Spotify for each song from the Billboard chart and adds the corresponding tracks to your newly created playlist.
4. **Playlist Management**: The playlist is created with the name based on the date you provided, and it's set to **private** by default.

---