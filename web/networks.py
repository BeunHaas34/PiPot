from wifi import Cell, Scheme


def getNetworks():
    #networks = list(Cell.all('wlan0'))
    networks = test()
    ssids = list(map(lambda x: x.ssid, networks))
    finalnetworks = []
    for ssid in ssids:
        finalnetworks.append((ssid, ssids.index(ssid)))
    ssids = [("1", 1), ("2", 2)]
    print(ssids)
    return ssids


def test():
    a = Cell()
    a.ssid = "networkA"
    b = Cell()
    b.ssid = "networkB"
    return [a, b]
