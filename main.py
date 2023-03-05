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
        SerialObj = serial.Serial('COM8')
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


# Close serial function
def closeSerial(SerialObj):
    SerialObj.close()


# Sound the Atticus alarm if turtle is nearby
def playAtticusAlarm():
    # Why so many slashes holy moly it's the slash slinging slasher
    playsound(r'C:\\\\Users\\\\brian\\\\PycharmProjects\\\\Squirtle\\\\mrfinch.mp3')


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

# Open the serial port for ESP32
esp = openSerial()

# Keep reading serial forever
while True:
    inserial = readSerial(esp)

    # If inserial receives a "close by" signal, alert the ship
    if (inserial > closest) and (inserial < toofar):
        print("Turtle nearby!")
        print("Please watch satellite feed for further details...")
        turtleAlarm(esp, audio=False)
        # For demo, if in "turtle nearby" range, plot these coordinates
        turtle_lat.append(-80.1337)
        turtle_lon.append(24.0744)
    # If inserial receives an "on top of" signal, sound the alarm and alert the ship
    elif inserial < closest:
        print("Turtle in range!")
        print(f"Turtle is {inserial} meters away from ship...")
        print("Alerting nearby ships!")
        turtleAlarm(esp, audio=True)
        # For demo, if in "turtle dead" range, plot these coordinates
        turtle_lat.append(-80.2843)
        turtle_lon.append(24.0003)
    # If inserial receives a "no turtles nearby" signal, do nothing
    else:
        print("No turtles in range, fish away.")
        # For demo, if in "good to go" range, plot these coordinates
        turtle_lat.append(-79.5819)
        turtle_lon.append(24.2615)
    plt.close()
    plotLatLon(turtle_lat, turtle_lon, ship_lat, ship_lon)
