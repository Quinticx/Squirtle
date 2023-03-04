import serial
from playsound import playsound
import os

# Open serial function
def openSerial():
    # Open the serial connection if it can be opened
    print("Opening serial port")
    try:
        SerialObj = serial.Serial('COM8')

    except serial.SerialException as err:
        print('An Exception Occured')
        print('Exception Details-> ', err)

    else:
        print("Serial port opened!")

        # Provide serial parameters
        SerialObj.baudrate = 115200  # set Baud rate to 115200
        SerialObj.bytesize = 8     # Number of data bits = 8
        SerialObj.parity   ='N'    # No parity
        SerialObj.stopbits = 1     # Number of Stop bits = 1
    return SerialObj

# Write serial function
def writeSerial(SerialObj):
    # Ship is too close to turtle, warn ship by transmitting the high signal
    print("Sending data to ship")
    # Write 1 to chip
    SerialObj.write(b'0')

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

# Open the serial port
esp = openSerial()
# Start inserial at 0 so module continuously looks for incoming distance alert
inserial = 0

# Keep reading serial if serial reads back "okay" (0)
while (inserial == 0):
    inserial = readSerial(esp)

    if (inserial == 1):
        print("Turtle detected!")
        print("Alerting nearby ships!")
        playAtticusAlarm()
        writeSerial(esp)
        inserial = readSerial(esp)


