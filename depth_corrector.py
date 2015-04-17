#Ar gradient correction program. Currently my data for an initial measurment of Ar consists of spots taken in a rough spiral at about 30 degress relative to the edge of my sample. I need to write a script that uses my image processing aloritum to define the edge of the sample and the position of the center of each spot on the sampe grid. Then I need it to measure he distance between each measurment point and the closest edge point, and input that number into a tuple with the intensity. This can be graphed to show relative Ar concentration as a function of depth.  
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
#im = Image.open('a_image.tif')
im = Image.open('7 points b.tif')
im2 = Image.open('7 points b.bmp')
pirate = np.asarray(im)
ship = np.asarray(im2) 
fleet = np.split(ship, [1,2], axis = 2)
ships = np.dsplit(ship, 3)
#print "dimensions of pirate are ", pirate.shape
#print "dimensions of ship are ", ship.shape
print "length of fleet is ", len(fleet)
print "length of ships is ", len(ships)
print fleet[0].shape, ship[0].shape
im4 = Image.fromarray(fleet[1])
#A = []
#B = []
#A = pirate[:,[800]]
#B = pirate[[30],:].T
#count = 0
#for i in B:
#    count = count + 1
#    print " vertical ", count," is", i
#print "A is vertical = ",A.shape
#print "B is horizontal = ",B.shape
#print "location 600, 800 pixel value is ", pirate[600,800]
#print "locaton 200, 300 pixel value is ", pirate[200,300]
pirate.setflags(write=1)#allows the matrix to be written on to change values. 
threshold = 110
pirate[pirate < threshold] = 0
pirate[pirate > threshold] = 200#this works, just couldn't distinguish 0 and 1 pixels
im3 = Image.fromarray(pirate)
im4.show()
#im.show()
#im3.show()


#function: replace all values with zero for off, and one for on the sample. Print the image to check if the threshold is ok. 