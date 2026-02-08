from datetime import date
import requests


def get_new_release(spotifyAPIUrl, TokenUrl, clientId, clientSecret, newReleaseData):

    r = requests.post(
        TokenUrl,
        data={
            "grant_type": "client_credentials",
            "client_id": clientId,
            "client_secret": clientSecret,
        }
    )

    if r.status_code != 200:
        print("Error: Failed to retrieve access token.")
        print(r.json())
        return newReleaseData

    token = r.json().get("access_token")
    if not token:
        print("Error: 'access_token' not found in the response.")
        return newReleaseData

    artistData = requests.get(
        spotifyAPIUrl,
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    if artistData.status_code != 200:
        print(f"Error: Failed to retrieve artist data. Status code: {artistData.status_code}")
        print(artistData.json())
        return newReleaseData

    artistDataJson = artistData.json()
    if "items" not in artistDataJson:
        print("Error: 'items' key not found in the response.")
        print(artistDataJson)
        return newReleaseData

    for item in artistDataJson["items"]:
        if item["release_date"] == date.today().strftime("%Y-%m-%d"):
            newReleaseData["newRelease"] = True
            newReleaseData["AlbumName"] = item["name"]
            newReleaseData["Type"] = item["album_type"]
            newReleaseData["releaseId"] = item["id"]
            newReleaseData["imageLink"] = item["images"][0]["url"]
            newReleaseData["albumUri"] = item["href"]

            for artist in item["artists"]:
                newReleaseData["Artists"] += artist["name"] + " & "

            newReleaseData["Artists"] = newReleaseData["Artists"][:-3]
            return newReleaseData
        else:
            newReleaseData["newRelease"] = False

    return newReleaseData


def get_songs_in_album(spotifyAPIUrl, TokenUrl, clientId, clientSecret):

    result = []
    r = requests.post(
        TokenUrl,
        data={
            "grant_type": "client_credentials",
            "client_id": clientId,
            "client_secret": clientSecret,
        }
    )

    if r.status_code != 200:
        print("Error: Failed to retrieve access token.")
        print(r.json())
        return result

    token = r.json().get("access_token")
    if not token:
        print("Error: 'access_token' not found in the response.")
        return result

    albumData = requests.get(
        spotifyAPIUrl,
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    if albumData.status_code != 200:
        print(f"Error: Failed to retrieve artist data. Status code: {albumData.status_code}")
        print(albumData.json())
        return result

    albumDataJson = albumData.json()


    for song in albumDataJson["tracks"]["items"]:
        artists = ""
        for artist in song["artists"]:
            artists += artist["name"] + " & "

        artists = artists[:-3]
        result.append([song["name"], artists])

    return result