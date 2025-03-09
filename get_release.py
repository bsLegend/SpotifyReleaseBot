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
            newReleaseData["Artist"] = item["artists"][0]["name"]
            return newReleaseData
        else:
            newReleaseData["newRelease"] = False
            newReleaseData["AlbumName"] = item["name"]
            newReleaseData["Type"] = item["album_type"]
            newReleaseData["Artist"] = item["artists"][0]["name"]

    return newReleaseData