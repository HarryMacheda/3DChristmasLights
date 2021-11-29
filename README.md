###################################################################################################################################################################################
# 3DChristmasLights
A way using a RaspberryPi, rpi_ws281x library, and laptop to get and use the 3d coordinates of ws281x LED's

WARNING! VERY BAD CODE AHEAD, WORKS DECENTLY BUT CAN DEFINITELY BE IMPROVED ON, I AM SORRY :)

The Repository contains 3 files:
main.py # File which interfaces with a raspberrypi using parimiko to photograph LEDS
/This is used to generate 3d Coordinates
/Raspberrypi must have a file which turns on the next LED everytime it is run
/Code will pause after it has taken photos of each LED at this point rotate object to next side 90 degrees, then click any key

ImageProcess.py #File which converts images into coordinate
/This outputs a text file in the format:
(x0,y0,z0)
(x1,y1,z1)
ect.

LightLibrary.py #Library which makes writing programs to control light easier
/information in file

###################################################################################################################################################################################
