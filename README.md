# Minecraft-To-Real-Life-ESP32
Detects conditions in Minecraft (via RCON) and triggers real-world actions on an ESP32

## Overview
This project takes information from a local minecraft server that the user is playing on using RCON and sends it to an ESP32 to trigger real world actions currently a buzzer beeping when damage is taken and 3 rapid beeps when below 3 hearts. As well as triggering a smart bulb when the player takes damage.

## Hardware Used
- ESP32
- Active Buzzer
- YeeLight Bulb

## Python Dependecies

- pip install mcrcon requests

## Setup

### 1. Minecraft Server
- Download and run minecraft server
- In server properties enable RCON, Set Rcon.port to 25575, set rcon.password to whatever you want
- Restart the server

### 2. ESP32
- Open the file in arduino IDE
- Enter your wifi credentials
- Upload to ESP32

### 3. Python
- Open the rcon_bridge.py file
- Fill in your RCON Password and IP Address
- Run the file

### 4. Yeelight Bulb
- Download the Yeelight app and connect your bulb
- In the bulb settings enable LAN Control
- Find the bulb's IP address in your router's device list
- Enter the IP in ESP32_Bridge.ino where it says yeelightIP
  
## Wiring
- Wire the buzzer to GPIO 13
