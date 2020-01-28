#########################################################################
# visualisation.py
#
# Minor Programming 
#
# Kiara Evers, Alessandro Degenkamp, Daniel Siha
#
# Bevat alle functies voor het visualiseren van de resultaten
##########################################################################

from matplotlib import pyplot as plt 
from code.writer import read_progress_run, delete_progress_run
import matplotlib.patches as patches
import numpy as np
import matplotlib.pyplot as plt




def visualisation(all_houses, waters):

    plt.xlabel('in meters')
    plt.ylabel('in meters')
    plt.title('map')
    plt.axis([0, 160, 0, 180])
    ground = plt.Rectangle((0,0), 160, 180, fc='forestgreen')      
    plt.gca().add_patch(ground)
    for water in waters:
        water = plt.Rectangle((water.bottom_left), water.bottom_right[0] - water.bottom_left[0], water.top_right[1] - water.bottom_left[1], fc='blue') 
        plt.gca().add_patch(water) 
   
    xx=[]
    yy=[]
    tekst=[]
    for key in all_houses.values():
        for house in key:
            if house.placed == True:
                xx.append(house.bottom_left[0])
                yy.append(house.bottom_left[1])
                tekst.append(str(house.name))
                if house.size == "small":
                    rectangle = plt.Rectangle(house.bottom_left, house.width, house.length, fc='purple',ec="green", linewidth=2)
                if house.size == "medium":
                    rectangle = plt.Rectangle(house.bottom_left, house.width, house.length, fc='yellow',ec="green", linewidth=3)
                if house.size == "large":
                    rectangle = plt.Rectangle(house.bottom_left, house.width, house.length, fc='red',ec="green", linewidth=6)       
                plt.gca().add_patch(rectangle)


    for i,tekst in enumerate(tekst):
        x = xx[i]
        y = yy[i]
        plt.scatter(x, y, marker='x', color='blue')
        plt.text(x, y, tekst, fontsize=12)

    plt.show()

def visualisation_plot(algoritme):
    xx = []
    yy = []
    x, y = read_progress_run()
    for item in x:
        coordinate = item
        coordinate = float(coordinate)
        xx.append(coordinate)

    for item in y:
        coordinate = item 
        coordinate = float(coordinate)
        yy.append(coordinate)
        
    plt.scatter(xx,yy, color='black', marker='o', alpha=0.4)
    
    plt.title('Returns per itteration', fontsize=15)
    plt.ylabel("total value map")
    plt.ticklabel_format(useOffset=False)
    ymin = min(yy)
    ymax = max(yy)
    plt.ylim(ymin - 100000, ymax + 100000)
    plt.axes().get_xaxis().set_visible(False)
    

    if algoritme == 1:
        plt.boxplot(yy)
    plt.show()
    
    delete_progress_run()