import serial
import time
ser = serial.Serial('/dev/ttyUSB0', 115200)


while True:
    ser.write('0'.encode('utf-8'))
    time.sleep(1)
    ser.write('1'.encode('utf-8'))
    time.sleep(1)

