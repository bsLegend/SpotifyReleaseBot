import json
import requests

with open("discordBotSettings.json", "r") as file:
    data = json.load(file)

channelId = data["channelId"]
botToken = data["botToken"]

def send_message(content):
    url = f"https://discord.com/api/v10/channels/{channelId}/messages"
    headers = {
        "Authorization": f"Bot {botToken}",
        "Content-Type": "application/json"
    }
    data = {
        "content": content
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200 or response.status_code == 201:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message: {response.status_code} - {response.text}")
