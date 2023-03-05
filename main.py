import serial
from playsound import playsound
import os

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
def writeSerial(SerialObj, distance):
    # Ship is too close to turtle, warn ship by transmitting the high signal
    print("Sending data to ship")
    # Write distance to chip
    SerialObj.write(distance)

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
    playsound(os.path.dirname(__file__) + '/mrfinch.mp3')

# Turtle alarm function
def turtleAlarm(esp, distance, audio=False):
    print("Turtle detected!")
    print("Alerting nearby ships!")
    if (audio == True):
        playAtticusAlarm()
    writeSerial(esp, distance)


# Constants
closest = 5
medium = 10
toofar = 15

# Open the serial port
esp = openSerial()
# Start inserial at greater than toofar so module continuously looks for incoming distance alert
inserial = toofar+1

# Keep reading serial if serial reads back "okay" (0)
while (inserial > toofar):
    inserial = readSerial(esp)

    # If inserial receives a "close by" signal, alert the ship
    if (inserial > closest) and (inserial < toofar):
        print("Turtle nearby!")
        print("Alerting nearby ships!")
        turtleAlarm(esp, inserial, audio=False)
        inserial = readSerial(esp)
    # If inserial receives a "on top of" signal, sound the alarm and alert the ship
    elif (inserial < closest):
        print("Turtle in range!")
        print("Alerting nearby ships!")
        turtleAlarm(esp, inserial, audio=True)
        inserial = readSerial(esp)
    else:
        print("No turtles in range, fish away.")


