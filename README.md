# PyDuino Bot
This is a Arduino(micro-controller)-based robot which is in the form of a rover consisting of a camera! It is controlled by a PyGame game(a python library) through WiFi.

## Components
The following components are required in order to make the robot:
```
1) Arduino Uno
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
