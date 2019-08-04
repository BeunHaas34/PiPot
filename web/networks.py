from wifi import Cell, Scheme

def getNetworks():
    networks = list(Cell.all('wlan0'))
    #networks = test()
    ssids = list(map(lambda x: x.ssid, networks))
    finalnetworks = []
    for ssid in ssids:
        tuple = (str(ssid), ssid)
        finalnetworks.append(tuple)
    return finalnetworks


def test():
    a = Cell()
    a.ssid = "networkA"
    b = Cell()
    b.ssid = "networkB"
    return [a, b]
