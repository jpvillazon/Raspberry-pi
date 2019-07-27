import smbus
import time

direccion = 0x48
cmd = 0x40
valor = 0
num=255

bus = smbus.SMBus(1)
while True:
    for i in range(1,256):
        bus.write_byte_data(direccion,cmd,valor)
        valor=i
        print("AOUT:%3d" %valor)
        time.sleep(0.01)

    for i in range(1,num+1):
        bus.write_byte_data(direccion,cmd,valor)
        valor=num-i
        print("AOUT:%3d" %valor)
        time.sleep(0.01)

