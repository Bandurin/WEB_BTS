import smbus
import time

# Access the i2c bus
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x04

def writeNumber(value):
    bus.write_i2c_block_data(address, 0, value)
    #bus.write_byte(address, value)
    return -1

def readNumber():
    number = bus.read_i2c_block_data(address, 0, 3)
    #number = bus.read_byte(address)
    return number


while True:
    var= [1, 100, 0]
    var1= [2, 100, 0]
 #   var2= [1, 190, 0]
    var3= [0, 0, 0]

    if not var:
       	continue

    writeNumber(var)
    time.sleep(3)

    writeNumber(var1)
    time.sleep(3)

  #  writeNumber(var2)
  #  time.sleep(2)

    writeNumber(var3)
    time.sleep(2)

    print ("var = RPI: Hi Arduino, I sent you ", var)
 #   print ("var = RPI: Hi Arduino, I sent you ", var1)
 #   print ("var = RPI: Hi Arduino, I sent you ", var2)
    number = readNumber()
    print ("Arduino: Hey RPI, I received a digit ", number)
    print

