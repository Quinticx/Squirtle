import serial
import time

# Open the serial connection if it can be opened
try:
    SerialObj = serial.Serial('COM11')

except serial.SerialException as err:
    print('An Exception Occured')
    print('Exception Details-> ', err)

else:
    print('Serial Port Opened')

    # Provide serial parameters
    SerialObj.baudrate = 9600  # set Baud rate to 9600
    SerialObj.bytesize = 8     # Number of data bits = 8
    SerialObj.parity   ='N'    # No parity
    SerialObj.stopbits = 1     # Number of Stop bits = 1

    time.sleep(3)

    # Write the test to chip
    SerialObj.write(b'A')

    SerialObj.close()
