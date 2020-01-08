from models import House, Water
from random import seed
from random import random
import _random
import math

# Import the necessary packages and modules vfor mathlibplot
import matplotlib.pyplot as plt
import numpy as np

#constants
ratio_small = 0,6
ratio_medium = 0,25
ratio_large = 0,15
maximum_height = 180
maximum_width = 160

def main():
    
    while True:
        number_of_houses = int(input("What are the amount of Houses?"))

        if number_of_houses > 0 and number_of_houses < 60:
            break

    number_small, number_medium, number_large = houses(number_of_houses)

    

    # returns a tuple of a cordinate x,y bottom left of house
    bottem_left = randomizer()

      # check if given cordinates overlap water
    if water.bottem_left[0] <= bottem_left[0] <= water.bottem_right[0] and water.top_left[1] <= bottom_left[1] <= water.bottem_right[1]:   
        break

    # check if given cordinates overlap houses/obligated space
    for house in houses:
        # add obligated space with surface of house
        if house.size == "small":
            houseandgarden_bottom_left[0] - 2
            houseandgarden_bottem_left[1] + 2
            houseandgarden_bottom_right[0] + 2
            houseandgarden_bottom_right[1] - 2
            houseandgarden_top_left[0] - 2
            houseandgarden_top_left[1] + 2
            houseandgarden_top_right[0] + 2
            houseanddgarden_top_right[1] + 2

            if houseandgarden_bottem_left[0] <= bottem_left[0] <= 
        
        if house.size == "medium":
            bottom_left[0] - 3
            bottem_left[1] + 3
        if house.size == "large":
            bottom_left[0] - 6
            bottem_left[1] + 6

    for small_house in number_small:
        small_house = House()

    for medium_house in number_medium


    # make visualisation
    plt.plot([x <= 160], [y <=180])
    plt.show()



    def randomizer():
        ''' Generates a random x and y value'''
        # Daniel wil seed later gebruiken, zorgt voor zelfde uitkomst okal random
        # Kiara eandgarden_wil math.floor verwijderen voor exacte cordinaten ipv grid
        random_x = math.floor(random()*maximum_height)
        random_y = math.floor(random()*maximum_width)
        return (random_x, random_y)

    def houses(number_of_houses):
        '''Determines number of houses per size house '''
        small = int(ratio_small * number_of_houses)
        medium = int(ratio_medium * number_of_houses)
        large = int(ratio_large * number_of_houses)
        
        return (number_small, number_medium, number_large)

    def createhouseobject(house_size, house_sort):
        list_of_objects = []

        if house_sort == "small":
            for i in range(house_size):
                small = House(size=small, start_value=285.000, obligated_space=2, rate=0.03, length=8, width=8)
                list_of_objects += small
        if house_sort == "medium":
            for i in range(house_size):
                small = House(size=medium, start_value=399.000, obligated_space=3, rate=0.04, length=11, width=7)
                list_of_objects += medium
        if house_sort == "large":
            for i in range(house_size):
                small = House(size=large, start_value=610.000, obligated_space=6, rate=0.06, length=12, width=10)
                list_of_objects += large
        

if __name__ == "__main__":
    main()


