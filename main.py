import serial
from playsound import playsound
import os
from gui import plotLatLon
import matplotlib.pyplot as plt

# Open serial function
def openSerial():
    # Open the serial connection if it can be opened
    print("Opening serial port")
    try:
        SerialObj = serial.Serial('COM7')
        # Provide serial parameters
        SerialObj.baudrate = 115200  # set Baud rate to 115200
        SerialObj.bytesize = 8  # Number of data bits = 8
        SerialObj.parity = 'N'  # No parity
        SerialObj.stopbits = 1  # Number of Stop bits = 1
        return SerialObj

    except serial.SerialException as err:
        print('An Exception Occured')
        print('Exception Details-> ', err)


# Write serial function
def writeSerial(SerialObj):
    # Ship is too close to turtle, warn ship by transmitting the high signal
    print("Sending data to ship")
    # Write to chip
    SerialObj.write(b'1')


# Read serial function
def readSerial(SerialObj):
    try:
        ser_bytes = SerialObj.readline()
        print("Receiving data from turtle")
        decoded_bytes = float(ser_bytes[0:len(ser_bytes) - 2].decode("utf-8"))
        return decoded_bytes
    except KeyboardInterrupt:
        print('Keyboard interrupted')


def closeSerial(SerialObj):
    SerialObj.close()


# Sound the Atticus alarm if turtle is nearby
def playAtticusAlarm():
    #playsound(os.path.dirname(__file__) + "/mrfinch.mp3")
    pass

# Turtle alarm function
def turtleAlarm(device, audio=False):
    if audio:
        playAtticusAlarm()
    writeSerial(device)


# Constants
closest = 2
medium = 4
toofar = 6

# Lat/Lons for Turtle
turtle_lat = []
turtle_lon = []
ship_lat = [-80.2843]
ship_lon = [24.0001]

# Open the serial port
esp = openSerial()

# Keep reading serial
while True:
    inserial = readSerial(esp)
    print(f"inserial: {inserial}")

    # If inserial receives a "close by" signal, alert the ship
    if (inserial > closest) and (inserial < toofar):
        print("Turtle nearby!")
        print("Alerting nearby ships!")
        turtleAlarm(esp, audio=False)
        turtle_lat.append(-80.1337)
        turtle_lon.append(24.0744)
    # If inserial receives an "on top of" signal, sound the alarm and alert the ship
    elif inserial < closest:
        print("Turtle in range!")
        print(f"Turtle is {inserial} away from ship...")
        print("Alerting nearby ships!")
        turtleAlarm(esp, audio=True)
        turtle_lat.append(-80.2843)
        turtle_lon.append(24.0003)
    # If inserial receives a "no turtles nearby" signal, do nothing
    else:
        print("No turtles in range, fish away.")
        turtle_lat.append(-79.5819)
        turtle_lon.append(24.2615)
    plotLatLon(turtle_lat, turtle_lon, ship_lat, ship_lon)


