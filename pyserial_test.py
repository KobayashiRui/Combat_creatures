import serial
ser = serial.Serial('/dev/ttyACM0',baudrate=9600,timeout=0.1)
while True:
    flag=bytes(input(),'utf-8')
    ser.write(flag)
    if(flag == bytes('q','utf-8')):
        break;
ser.close()
