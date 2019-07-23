import subprocess, sys, re
import threading

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
            check(message)

def check(message):
    if 'associated' in message and 'disassociated' not in message:
        print(message)