import requests
import time
from time import gmtime, strftime
while True:
    if strftime("%S") == "00":
        payload = '{"custom_status":{"text":"' + strftime("%I:%M %p | %y-%m-%d ⏰", time.localtime()) + '","emoji_name":"⏰"}}'
        requests.patch("https://discordapp.com/api/v6/users/@me/settings", payload.encode("utf-8",),
            headers={
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-GB",
                "authority": "discordapp.com",
                "authorization": "!YOUR AUTH KEY HERE!",
                "content-type": "application/json",
                "origin": "https://discordapp.com",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.9 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36",
            },
        )
