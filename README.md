<div align = "center">
  <h1>
    PyDuino Bot
  </h1>
</div>

A set of programs used in an Arduino(micro-controller / µC)-based robot resembling a rover! It can detect human faces using Computer Vision and is controlled by a game developed using the Pygame(a python library) through WiFi.

<img src = "https://github.com/Omanshu209/PyDuino_Bot-WiFi/assets/114089324/9b48e359-6331-4f03-a752-2240e92f1ba8" width = "400px" align = "right" />

## Components
The following components are required in order to make the robot:
```
1) Arduino Uno (µC)
2) ESP-32 CAM Module
3) OV2680 Camera Module
4) L298N motor Driver
5) Jumper Wires
6) 2 DC Motors(Geared)
7) 4 Wheels
8) 9V battery
9) 9V battery connector
10) Breadboard
11) Arduino programmable cable
```
<img src = "https://github.com/Omanshu209/PyDuino_Bot-WiFi/assets/114089324/77762e4c-4e94-44f9-ac77-69f938904d82" width = "400px" align = "left" />

## Uploading the Code
```
- Upload the 'ESP32_MAIN.ino' file available in the ESP32 folder to the ESP-32 CAM trough UART connection
(Upload using the Arduino IDE in windows or the Arduino Droid app in android)
```
## Curcuit
```
- Connect the wheels to the motors
- Connect the OV2680 Camera Module to the ESP-32 CAM
```
```
Positive terminal (Motor 1) --> OUT 1 (L298 motor driver)
Negative terminal (Motor 1) --> OUT 2 (L298 motor driver)
Positive terminal (Motor 2) --> OUT 4 (L298 motor driver)
Negative terminal (Motor 2) --> OUT 3 (L298 motor driver)

PIN 1 (L298N motor driver)  --> IO12 (ESP-32 CAM)
PIN 2 (L298N motor driver)  --> IO13 (ESP-32 CAM)
PIN 3 (L298N motor driver)  --> IO15 (ESP-32 CAM)
PIN 4 (L298N motor driver)  --> IO14 (ESP-32 CAM)

12V (L298N motor driver)    --> Negative terminal (9V battery)


                             ---> GND (ESP-32 CAM)
                             |
GND (L298N motor driver)    --
                             |
                             --> Positive terminal (9V battery)


UnR (ESP-32 CAM)   --> RX (Arduino Uno)
UoT (ESP-32 CAM)   --> TX (Arduino Uno)
GND (ESP-32 CAM)   --> GND (Arduino Uno)

REST (Arduino Uno) --> GND (Arduino Uno)


5V (L298N motor driver) --> Breadboard --
                                         |
5V (ESP-32 CAM)         --> Breadboard ----> Series connection
                                         |
5V (Arduino Uno)        --> Breadboard --
```
## Usage
```
- Change your WiFi's/Hotspot's name to 'username' and password to 'password'
- Turn on your WiFi/Hotspot
- Connect the Arduino Uno to your device using the Arduino cable
- Open the monitor of the Arduino IDE/Arduino Droid app
- Change the Baud rate to 115200
- Press the reset button of the ESP-32 CAM module
- An IP address will be visible in the monitor of the IDE/App
- Open the IP address(https://IP_address) to access the camera
- To move the robot run the main.py file available in the Python folder and play the game!
```
![Screenshot_2023-05-07-12-40-46-737](https://github.com/Omanshu209/PyDuino_Bot-WiFi/assets/114089324/c21db83d-c390-4365-b183-1ec440a2acb4)

## Credits
This project was created by **Omanshu**.
