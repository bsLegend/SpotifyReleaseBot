import json
from get_release import get_new_release
from send_message import send_message

artistIds = []

try:
    with open("artists.json", "r") as file:
        data = json.load(file)

    if "artistIds" in data:
        artistIds = data["artistIds"]
    else:
        raise KeyError("The JSON file does not contain a key named 'artistIds'. Please check the file structure.")

except FileNotFoundError:
    print("Error: The file 'artists.json' was not found. Please ensure the file exists in the correct directory.")
except json.JSONDecodeError:
    print("Error: Failed to decode JSON. Please ensure 'artists.json' is properly formatted.")

alreadyMessaged = []

try:
    with open("alreadyMessaged.json", "r") as file:
        alreadyMessagedData = json.load(file)

    if "alreadyMessaged" in alreadyMessagedData:
        alreadyMessaged = alreadyMessagedData["alreadyMessaged"]
    else:
        raise KeyError("The JSON file does not contain a key named 'alreadyMessaged'. Please check the file structure.")

except FileNotFoundError:
    print("Error: The file 'alreadyMessaged.json' was not found. Please ensure the file exists in the correct directory.")
except json.JSONDecodeError:
    print("Error: Failed to decode JSON. Please ensure 'alreadyMessaged.json' is properly formatted.")


TokenUrl = "https://accounts.spotify.com/api/token"

with open("secret.json", "r") as config_file:
    config = json.load(config_file)
    clientId = config["clientId"]
    clientSecret = config["clientSecret"]


newReleaseData = {
    "newRelease": False,
    "Artist": "",
    "AlbumName": "",
    "Type": ""
}

for artistId in artistIds:
    spotifyAPIUrl = f"https://api.spotify.com/v1/artists/{artistId}/albums"
    get_new_release(spotifyAPIUrl, TokenUrl, clientId, clientSecret, newReleaseData)
    for items in alreadyMessaged:
        if items == f"{newReleaseData['Artist']}{newReleaseData['AlbumName']}{newReleaseData['Type']}":
            newReleaseData["newRelease"] = False
            break
    if newReleaseData["newRelease"] is True:
        message = f"New Release from {newReleaseData['Artist']}:\n{newReleaseData['AlbumName']}\n{newReleaseData['Type']}"
        send_message(message)

        alreadyMessagedData["alreadyMessaged"].append(
            f"{newReleaseData['Artist']}{newReleaseData['AlbumName']}{newReleaseData['Type']}")

        with open("alreadyMessaged.json", "w") as file:
            json.dump(alreadyMessagedData, file, indent=4)
