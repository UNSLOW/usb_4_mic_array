
from tuning import Tuning
import usb.core
import usb.util
import time
import socket

HOST = '127.0.0.1'
PORT = 10000

dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)
#print dev
if dev:
    Mic_tuning = Tuning(dev)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('Addr:{}'.format( (HOST,PORT) ))
    print('Press CTRL+C to end.')

    while True:
        try:
            text= str.format('{},{}',Mic_tuning.direction, Mic_tuning.is_voice())
            print( text )
            sock.sendto( bytes(text,'utf-8'), (HOST, PORT) )
            time.sleep(1)
        except KeyboardInterrupt:
            print('Ctrl+C')
            break

    sock.close()

    print('Done.')
