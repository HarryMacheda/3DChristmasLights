# Library to Help with the rpi_ws281x Library
import math
#This Imports Coordinates into an Array
#From TXT FIle with each line (x,y,z)
def Import_Coordinates(File_Name,LED_Count):
    Coord_Array = []
    CoordsTXT = open(File_Name, "r")
    Coord_Lines = CoordsTXT.readlines()
    for i in range(LED_Count):
        temp = []
        string = Coord_Lines[i]
        string = string[1:-1]  # 406, 181, 0
        string1 = string.partition(",")[0]
        string = string[len(string1) + 1:]
        string2 = string.partition(",")[0]
        string = string[len(string2) + 1:]
        string = string[:-1]
        string3 = string
        temp.append(int(string1))
        temp.append(int(string2))
        temp.append(int(string3))
        temp.append(0)
        Coord_Array.append(temp)
    return(Coord_Array)

#This Returns the distance from two arrays of Length N
def Calc_Distance(Point1, Point2):
    distance = []
    for i in range(len(Point1)):
        distance.append(math.pow(Point2[i]-Point1[i],2))
    return math.sqrt(sum(distance))

#Converts an array to a colour for the LED
def array2Colour(array):
    return Color(int(array[0]),int(array[1]),int(array[2]))

#Calculates the gradient over a number of steps between two N dimensional arrays
def Gradient(Array1,Array2,Steps):
    gradient = []
    for i in range(len(Array1)):
        gradient.append((Array2[i]-Array1[i])/(Steps-1))
    return gradient

#Generates an array of N dimensional arrays which smoothly transition from array1 to array2 in Steps steps
def Generate_Wheel(Array1,Array2,Steps):
    gradient = Gradient(Array1,Array2,Steps)
    Wheel = []
    for i in range(Steps):
        Temp = []
        for j in range(len(Array1)):
            Temp.append(Array1[j]+(i*gradient[j]))
        Wheel.append(Temp)
    return Wheel