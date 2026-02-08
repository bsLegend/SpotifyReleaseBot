import json
from get_release import get_new_release, get_songs_in_album
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
    "Artists": "",
    "AlbumName": "",
    "Type": "",
    "releaseId": "",
    "imageLink": "",
    "albumUri": "",
}

isAlbum = False

for artistId in artistIds:
    spotifyAPIUrl = f"https://api.spotify.com/v1/artists/{artistId}/albums"
    get_new_release(spotifyAPIUrl, TokenUrl, clientId, clientSecret, newReleaseData)

    for item in alreadyMessaged:
        if item == f"{newReleaseData["releaseId"]}":
            newReleaseData["newRelease"] = False
            break

    if newReleaseData["Type"] == "album":
        isAlbum = True

    if newReleaseData["newRelease"] is True:
        message = f"{newReleaseData['Artists']}\n{newReleaseData['AlbumName']}"
        if isAlbum:
            songs = get_songs_in_album(newReleaseData["albumUri"], TokenUrl, clientId, clientSecret)
            message += "\n\nSongs:\n"
            for song in songs:
                message += f"\n **{song[0]}**\n└ *{song[1]}*"
            send_message("Album", message, newReleaseData["imageLink"])
        else:
            send_message("Single", message, newReleaseData["imageLink"])

        alreadyMessagedData["alreadyMessaged"].append(
            f"{newReleaseData["releaseId"]}")

        with open("alreadyMessaged.json", "w") as file:
            json.dump(alreadyMessagedData, file, indent=4)
