from whois import whois
from datetime import datetime
import requests
from settings import *


def sendMessage(message):
    data = {
        "content": message,
        "username": "watchdog"
    }

    response = requests.post(WEBHOOK_URL, json=data)

    if response.status_code == 204:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message: {response.status_code}")


def timedelta_to_ymd(delta):
    days = delta.days

    years = days // 365
    days %= 365

    months = days // 30  # Approximate month as 30 days
    days %= 30

    return years, months, days

def main():
    whois_data = whois(DOMAIN)
    expiration_date = whois_data.expiration_date
    now = datetime.now()

    delta = expiration_date - now

    if (delta < 0):
        sendMessage("ドメイン切れてます")
        return
    
    years, months, days = timedelta_to_ymd(delta)
    sendMessage(f"{str(years) + '年' if years != 0 else ""}{str(months) + 'ヶ月' if months != 0 else ""}{days}日でドメインが切れます。")


if __name__ == "__main__":
    main()
