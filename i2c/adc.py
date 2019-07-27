import smbus
import time

miADC = smbus.SMBus(1)

def leeINPUT(X):
	miADC.write_byte_data(0x48, (0x40 + X),X)
	time.sleep(0.2)
	lectura = miADC.read_byte(0x48)
	return lectura

while True:
    an1 = leeINPUT(0)
    print (an1)

