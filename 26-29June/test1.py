import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
	port='/dev/ttyACM1',
	baudrate=9600
)

#ser.open()
ser.isOpen()

reading = 0

while 1 :

	if ser.inWaiting() > 0:
		reading = ord(ser.read(1))

		print reading

ser.close()
