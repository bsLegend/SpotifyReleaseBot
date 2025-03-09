# SpotifyReleaseBot
This is a Python-based script that checks for new releases by specific artists on Spotify and sends a notification using Discord. The repository integrates the Spotify REST API and a Discord bot for seamless updates.
## Features
- Fetches album releases from Spotify for specified artists.
- Utilizes Spotify's **API** for fetching artist and album details.
- Sends updates about newly released albums or singles via a Discord bot.
- Easy configuration using **JSON** files for artist and bot credentials.

## Requirements
To use this project, you need the following:
- **Python 3.10+**
- `requests` library (pre-installed or added via pip):
``` bash
  pip install requests
```
- A valid Spotify Developer account for API credentials.
- A Discord bot token and permissions to send messages in your server.

## Setup Instructions
### Step 1: Clone the Repository
Clone the project to your local machine:
``` bash
git clone https://github.com/your_username/spotify-new-release-notifier.git
cd spotify-new-release-notifier
```
### Step 2: Obtain Spotify API Credentials
1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2. Create a new app and note the **client ID** and **client secret**.

### Step 3: Configure JSON Files
1. Create a `secret.json` file for Spotify credentials:
``` json
    {
      "clientId": "<YOUR_SPOTIFY_CLIENT_ID>",
      "clientSecret": "<YOUR_SPOTIFY_CLIENT_SECRET>"
    }
```
1. Create an `artists.json` file to define the artists to monitor:
``` json
    {
      "artistIds": ["<ARTIST_ID_1>", "<ARTIST_ID_2>"]
    }
```
- Replace `<ARTIST_ID>` with the unique Spotify ID of the artists you want to track. You can find these IDs via the Spotify web app by copying the last part of an artist’s profile URL.

### Step 4: Obtain Discord Bot Token and Channel ID
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications), create a bot, and copy the bot token.
2. Add the bot to your server via OAuth2, as described in the guide.
3. Right-click your target channel in Discord, enable Developer Mode, and select **Copy ID** to get the channel ID.

### Step 5: Add Discord Bot Configuration
Update the script to include your bot token and channel ID in the appropriate variables:
- Add these at the start of your Python script:
``` python
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHANNEL_ID = "YOUR_CHANNEL_ID"
```
## Running the Script
1. Run the project from the command line:
``` bash
    python main.py
```
1. The script will:
    - Use the Spotify API to check for new releases from the artists in `artists.json`.
    - Send a message to your specified Discord channel if a new release is detected.

## Example Output
When a new release is detected, the bot sends a message in your Discord channel:
``` 
New Release from Ken Carson:
A Great Chaos
album
```
## Troubleshooting
1. **Spotify API Errors**:
    - Ensure your `clientId` and `clientSecret` are correct in `secret.json`.
    - Check if the Spotify access token has expired (you may need to refresh when long sessions are used).

2. **Discord API Errors**:
    - Confirm the bot has permissions to send messages in the target channel.
    - Ensure the `BOT_TOKEN` and `CHANNEL_ID` values are correct.

3. **General Python Errors**:
    - Missing dependencies can be installed using:
``` bash
      pip install -r requirements.txt
```
- Syntax issues? Ensure you're running **Python 3.10 or later**.

## Contributing
Contributions are welcome! If you find a bug or would like to add a feature, please:
1. Fork the repository.
2. Create a new branch:
``` bash
   git checkout -b feature-name
```
1. Submit a pull request when ready.

## License
This project is licensed under the Apache-2.0 License. See the [LICENSE](LICENSE) file for more details.
## Acknowledgments
- **Spotify Developer API**: For enabling seamless integration with music data.
- **Discord API**: For providing an easy-to-use platform for messaging.
