#Ar gradient correction program. Currently my data for an initial measurment of Ar consists of spots taken in a rough spiral at about 30 degress relative to the edge of my sample. I need to write a script that uses my image processing aloritum to define the edge of the sample and the position of the center of each spot on the sampe grid. Then I need it to measure he distance between each measurment point and the closest edge point, and input that number into a tuple with the intensity. This can be graphed to show relative Ar concentration as a function of depth.  
import numpy as np
import csv
from PIL import Image
from matplotlib import pyplot as plt

def distance_calculator(x_value_1, y_value_1, X, Y, point_number):
    count = 0
    distances = []
    while count < len(X):
        x_value_2 = int(X[count])
        y_value_2 = int(Y[count])
#        print "type x_value_1 is", type(x_value_1)
#        print "type y_value_1 is", type(y_value_1)
#        print "type x_value_2 is", type(x_value_2)
#        print "type y_value_2 is", type(y_value_2)        
#        print "x_value_2 type is ", x_value_2#add check type function!
#        print "y_value_2 is ", y_value_2#add check type function!
        distance = np.sqrt(np.square(x_value_1-x_value_2)+np.square(y_value_1-y_value_2))#breaks here. the x_value_1 and x_value_2 may be of different types. 
        distances.append(distance)
        count = count + 1
    point_stats = [point_number,min(distances)]
    #print "point_stats are ", point_stats
    return point_stats

def distance_to_surface(layer_1):
    distances_data = []
    ind_offsample = np.where(layer_1 == 0)  
    X,Y = ind_offsample
    with open('Ar_microprobe_spots_3_18_15.csv', 'rb') as csvfile:
        pirate = csv.reader(csvfile, delimiter = ',')
        next(pirate)
        for row in pirate:
            point_number = row[0]
            x_value_1 = int(row[1])#add check type function!
            y_value_1 = int(row[2])#add check type function!
            point_stats = distance_calculator(x_value_1, y_value_1, X, Y, point_number)
            distances_data.append(point_stats)
    print distances_data


def depth_corrector_main():
    im = Image.open('Ar_grad_3_18_15.tif')        
    image_map = np.asarray(im)
    image_map.setflags(write=1)#allows the matrix to be written on to change values. 
    threshold = 110
    image_map[image_map < threshold] = 0
    image_map[image_map > threshold] = 255
    layer_1,layer_2,layer_3 = np.dsplit(image_map,3)
    layer_1 = np.reshape(layer_1, (733, 984))
    layer_2 = np.reshape(layer_1, (733, 984))
    layer_3 = np.reshape(layer_1, (733, 984))
    distance_to_surface(layer_1)
 
    print "ind_offsample lengths are", len(ind_offsample[0]), len(ind_offsample[1])
      
    threshold_test_image = Image.fromarray(image_map)
    layer_1_test = Image.fromarray(layer_1)
    layer_2_test = Image.fromarray(layer_2)
    layer_3_test = Image.fromarray(layer_3)
    layer_1_test.show()
    layer_2_test.show()
    layer_3_test.show()

depth_corrector_main()
