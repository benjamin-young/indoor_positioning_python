import json
from os import access
import numpy as np
import matplotlib.pyplot as plt
import random 

accessPointIDs = []

#size of map
n=5
m=25
EMFMap =  [[0]*m for i in range(n)]
WifiMap = [[[0]*m for i in range(n)] for i in range(len(accessPointIDs))]


def loadMaps():
    with open('signalmapping-default-rtdb-export-2.json', 'r') as f:
        data = json.load(f)

    for reading in data:
        #print(reading)
        X = int(reading.split(',')[0])
        Y = int(reading.split(',')[1])
        Direction = int(reading.split(',')[2])

        if(Direction < -50):
            result = data[reading]
            for key in result:
                #EMF map
                if(key == "magH"):
                    EMFMap[X][Y] = result[key]
                    #print(result[key])

                #WIFI map
                if(key == "scanResults"):
                    wifiList = result[key]
                    for accessPoint in wifiList:
                        id = str(accessPoint.split(',')[1]).strip()
                        strength = str(accessPoint.split(",")[2]).strip()
                        #print(id)
                        if id not in accessPointIDs:
                            accessPointIDs.append(id)
                            WifiMap.append([[0]*m for i in range(n)])
                        
                        #print(accessPoint)
                        WifiMap[accessPointIDs.index(id)][X][Y] = int(strength)

def visualiseMaps():
    fig, axs = plt.subplots(2,2)
    wifiMapNP = np.array(WifiMap)
    EMFMapNP = np.array(EMFMap)

    axs[0, 0].set_title(accessPointIDs[0])
    im1 = axs[0, 0].imshow(wifiMapNP[0])

    axs[0, 1].set_title(accessPointIDs[1])
    im2 = axs[0, 1].imshow(wifiMapNP[1])

    axs[1, 0].set_title(accessPointIDs[5])
    im3 = axs[1, 0].imshow(wifiMapNP[5])

    axs[1, 1].set_title("EMF")
    im4 = axs[1, 1].imshow(EMFMapNP)

    plt.show()

def estimateLocation(reading):
    x = random.randint(0,m)
    y = random.randint(0,n)


    return [x,y]

loadMaps()

newReading = {
  "0,0,160": {
    "magH": 40.81758139787161,
    "magX": -7.9375,
    "magY": -32.678749084472656,
    "magZ": -23.13374900817871,
    "scanResults": [
      "eduroam, 54:78:1a:73:a2:61, -59",
      "central, 54:78:1a:73:a2:60, -58",
      "eduroam, b8:be:bf:ef:4e:a1, -80",
      "central, b8:be:bf:ef:4e:a0, -81",
      "central, 00:1b:8f:88:9a:ef, -90",
      "central, 54:78:1a:21:3b:cf, -64",
      "eduroam, 54:78:1a:21:3b:ce, -55",
      "DIRECT-XDDAVIDSSURFACEmsFv, ba:31:b5:86:9a:28, -74",
      "central, 54:78:1a:21:3b:c0, -58",
      "eduroam, 54:78:1a:21:3b:c1, -59",
      "central, 00:1b:8f:88:9a:e0, -85",
      "eduroam, 00:1b:8f:88:9a:e1, -87",
      "central, 6c:99:89:0d:91:4f, -56",
      "eduroam, 6c:99:89:0d:91:4e, -58",
      "eduroam, 54:78:1a:73:a2:6e, -71",
      "central, 54:78:1a:73:a2:6f, -71",
      "central, 6c:99:89:0d:91:40, -55",
      "eduroam, 6c:99:89:0d:91:41, -54"
    ]
  }
}

print(estimateLocation(newReading))
