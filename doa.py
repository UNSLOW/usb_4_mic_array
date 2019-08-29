
from tuning import Tuning
from datetime import datetime
import usb.core
import usb.util
import time
import socket

HOST = '127.0.0.1'
PORT = 10100

dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)

if dev is None:
    print("Device not found.")

else:
    Mic_tuning = Tuning(dev)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('Addr:{}'.format( (HOST,PORT) ))
    print('Starting:{}'.format(datetime.now().isoformat()))
    print('Press CTRL+C to end.')

    while True:
        try:
            b = 'True' if Mic_tuning.is_voice() else 'False'
            t = datetime.now().isoformat()
            text= str.format('{},{},{}',Mic_tuning.direction, b, t)
            sock.sendto( bytes(text,'utf-8'), (HOST, PORT) )
            print(text)
            time.sleep(0.05)
        except KeyboardInterrupt:
            print('Ctrl+C')
            break

    sock.close()

    print('Done.')
