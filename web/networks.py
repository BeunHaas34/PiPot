from wifi import Cell, Scheme

def getNetworks():
    networks = list(Cell.all('wlan0'))
    ssids = list(map(lambda x: x.ssid, networks))
    finalnetworks = []
    for ssid in ssids:
        finalnetworks.append((ssid, ssid))
    print(ssids)
    return ssids