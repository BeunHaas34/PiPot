import subprocess, sys, re
import threading
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

command = '/home/pi/hostapd-mana/hostapd/hostapd /home/pi/hostapd-mana/hostapd/hostapd.conf'

def capture():
    print('Function called: scanner.py/capture()')
    x = threading.Thread(target=runCapture)
    x.start()

def runCapture(cmd=command):
    print('Function called: scanner.py/runcapture()')
    capture_process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)

    while True:
        out = capture_process.stdout.readline()
        if out == '' and capture_process.poll() != None:
            break
        if out != '':
            message = out.decode("utf-8")
            check(message.rstrip())

def check(message):
    if 'associated' in message and 'disassociated' not in message:
        regex = '(.*)([a-zA-Z0-9]{2}:[a-zA-Z0-9]{2}:[a-zA-Z0-9]{2}:[a-zA-Z0-9]{2}:[a-zA-Z0-9]{2}:[a-zA-Z0-9]{2})(.*)'
        mac_search = re.search(regex, message, re.IGNORECASE)
        if mac_search:
            mac = mac_search.group(2)

            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)('stream', {'message': mac})
            print(mac)