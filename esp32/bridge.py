import time
import requests
from mcrcon import MCRcon

RCON_HOST = "localhost"
RCON_PASSWORD = "yourpasswordhere"
ESP32_IP = "###.###.##.##"
POLL_INTERVAL = 0.5

def get_health(mcr):
    resp = mcr.command("/data get entity @p Health")
    try:
        return float(resp.split(":")[-1].strip().replace("f", ""))
    except:
        return None

def get_hunger(mcr):
    resp = mcr.command("/data get entity @p foodLevel")
    try:
        return int(resp.split(":")[-1].strip())
    except:
        return None

with MCRcon(RCON_HOST, RCON_PASSWORD) as mcr:
    print("Connected to Minecraft RCON")
    while True:
        health = get_health(mcr)
        hunger = get_hunger(mcr)
        if health is not None and hunger is not None:
            print(f"Health: {health}/20  |  Hunger: {hunger}/20")
            try:
                url = f"http://{ESP32_IP}/update?health={health}&hunger={hunger}"
                print(f"Sending: {url}")
                requests.get(url, timeout=1)
            except:
                print("ESP32 not reachable")
        time.sleep(POLL_INTERVAL)
