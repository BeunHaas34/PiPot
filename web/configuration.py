import fileinput, os
from shutil import copyfile
from web.scanner import capture
from PiPot.settings import STATICFILES_DIRS

text_to_search = "<<NETWORKNAME>>"
sourceHostapd = os.path.join(STATICFILES_DIRS[0], 'hostapd.conf')
targetHostapd = "/home/pi/hostapd-mana/hostapd/hostapd.conf"

def saveConfig(networkName):
    if os.path.exists(targetHostapd):
      os.remove(targetHostapd)

    if os.path.exists(sourceHostapd):
        
        copyfile(sourceHostapd, targetHostapd)
    else:
        print("Warn! No source hostapd.conf file found in '"+ sourceHostapd +"'")
        return False

    # Read in the file
    with open(targetHostapd, 'r') as file :
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(text_to_search, networkName)

    # Write the file out again
    with open(targetHostapd, 'w') as file:
        file.write(filedata)

    capture()