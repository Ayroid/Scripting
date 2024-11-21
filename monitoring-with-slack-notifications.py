import requests
from constants import SERVER_URL, WEBHOOK_URL

def monitor_server_health(server_url, slack_webhook):
  try:
    response = requests.get(server_url)

    if response.status_code == 200 or response.status_code == 304:
      message = f"Server {server_url} is up and running!"
    else:
      message = f"Server {server_url} is down! Status code: {response.status_code}"

    slack_data = {'text': message}
    slack_response = requests.post(slack_webhook, json=slack_data)

    if slack_response.status_code == 200:
      print("Notification sent successfully!")
    else:
      print(f"Failed to send notification! Status code: {slack_response.status_code}")

  except requests.exceptions.RequestException as e:
    print(f"Failed to connect to server {server_url}! Error: {e}")
    error_message = f"Failed to connect to server {server_url}! Error: {e}"
    slack_data = {'text': error_message}
    slack_response = requests.post(slack_webhook, json=slack_data)

monitor_server_health(SERVER_URL, WEBHOOK_URL)