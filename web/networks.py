from wifi import Cell, Scheme

def getNetworks():
    networks = list(Cell.all('wlan0'))
    ssids = list(map(lambda x: x.ssid, networks))
    return ssids