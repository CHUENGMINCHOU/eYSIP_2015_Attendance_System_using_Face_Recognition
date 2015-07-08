import serial
import time

ceilingHeight = 177


ser = serial.Serial(
	port='/dev/ttyACM0',
	baudrate=9600
)


def getHeight():
    if ser.isOpen():
        ser.write('s')
        while(1):
            if ser.inWaiting() > 0:
                break
            
        temp = ord(ser.read(1))
        return ceilingHeight - temp 
	#Serial port not open exception
    else:
        return 1000

def greenOn():
    if ser.isOpen():
        ser.write('g')

def greenOff():
    if ser.isOpen():
        ser.write('G')

def redOn():
    if ser.isOpen():
        ser.write('r')

def redOff():
    if ser.isOpen():
        ser.write('R')


def closeSerial():
    ser.close()

