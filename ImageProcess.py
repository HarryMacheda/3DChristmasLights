import numpy as np
import argparse
import cv2
import time

file = open("Coordinates.txt","w")
file.write("")
file.close()


LED_COUNT = 500
SIZE = [0,0] #stores the size of the image for flipping coords
#Logic which finds the Coordinates of the brightest spot and value of brightness
CoordArray = [] #Stores the location of the brightest spot LED*4*2
BrightnessValue = [] #stores the brightness value LED*4*1
for i in range(LED_COUNT):
    tempc = []
    tempb = []
    for j in range(4):
        path = "{SET}".format(SET=j + 1) + "{LED}.png".format(LED=i)
        image = cv2.imread(path)
        h, w, c = image.shape
        SIZE[0] = h
        SIZE[1] = w

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
        tempc.append(str(maxLoc))
        tempb.append(int(maxVal))

    CoordArray.append(tempc)
    BrightnessValue.append(tempb)

CoordArrayInt = [] #Stores the integer values of coords
## Converting the coordinates into integer values
for i in range(LED_COUNT):
    temp1 = []
    for j in range(4):
        temp = []
        string = CoordArray[i][j]
        string = string[1:-1]  # 406, 181, 0
        string1 = string.partition(",")[0]
        string = string[len(string1) + 2:]
        string2 = string.partition(",")[0]
        string = string[len(string2)+2:]
        string = string[:-1]
        string3 = string
        temp.append(int(string1))
        temp.append(int(string2))
        temp1.append(temp)
    CoordArrayInt.append(temp1)
#Flip the Coordinates to get right dimensions
#Only flip first and second coords
for i in range(LED_COUNT):
    for j in range(2):
        CoordArrayInt[i][j][0]= SIZE[1]-CoordArrayInt[i][j][0]


AnalyCoord = []
#Calculate Actual Coordinate
for i in range(LED_COUNT):
    tempCoord = [0,0,0]
    #Load Values into variables
    Coord1 = CoordArrayInt[i][0] #Coords of first picture
    Coord2 = CoordArrayInt[i][1]#^^
    Coord3 = CoordArrayInt[i][2]#^^
    Coord4 = CoordArrayInt[i][3]#^^
    Bright1 = BrightnessValue[i][0] #Brightness value of coords
    Bright2 = BrightnessValue[i][1]
    Bright3 = BrightnessValue[i][2]
    Bright4 = BrightnessValue[i][3]
    #Get Coords of whichever photo is brightest
    tempy = []
    if Bright1>Bright3:
        tempCoord[0] = Coord1[0]
        tempy.append(Coord1[1])
    else:
        tempCoord[0] = Coord3[0]
        tempy.append(Coord3[1])

    if Bright2>Bright4:
        tempCoord[2] = Coord2[0]
        tempy.append(Coord2[1])
    else:
        tempCoord[2] = Coord4[0]
        tempy.append(Coord4[1])
    tempCoord[1] = int(sum(tempy)/2)
    AnalyCoord.append(tempCoord)

for i in range(LED_COUNT):
    file = open("Coordinates.txt", "a")
    file.write(str(AnalyCoord[i])+"\n")
    file.close()