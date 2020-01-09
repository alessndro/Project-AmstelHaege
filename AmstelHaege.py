from models import House, Water
from random import seed
from random import random
import _random
import math
import csv
#from coede.visualitastion import visualise as vis

# Import the necessary packages and modules for matplotlib
import matplotlib.pyplot as plt
import numpy as np

#constants
ratio_small = 0,6
ratio_medium = 0,25
ratio_large = 0,15
maximum_height = 180
maximum_width = 160
width_length_small_house = 8

def main():
    
    # ask user for number of houses to be placed
    while True:
        number_of_houses = int(input("What are the amount of Houses?"))

        if number_of_houses > 0 and number_of_houses < 60:
            break

    # determine division houses
    number_small, number_medium, number_large = ratio_houses(number_of_houses)

    # make visualisation


    # create list of objects
    small_houses = create_house_object(number_small, "small")
    medium_houses = create_house_object(number_medium, "medium")
    large_houses = create_house_object(number_large, "large")
    
    # save lists in dictionary
    # all_houses = {}
    all_houses[small] = small_houses
    all_houses[medium] = medium_houses
    all_houses[large] = large_houses
    
    for house in all_houses[large]
    # returns a tuple of a cordinate x,y bottom left of house
    bottem_left = randomizer()
    house.location(bottem_left)

    # vul object huis in met bottem_left coordinaten
    def fill_information_house(bottem_left, house)
    '''Vult alle coordinaten in van het object op basis van het random punt dat is gekozen ''' 
        if house_size == small:
            count = 0
            for i in range(8):
                for j in range(8):
                    bottem_left(: + i ,: + j) = "s" + count
                    count += 1

    def place_house(selected_house):
    '''Bepaald of een huis op de gekozen locatie geplaatst kan worden '''
    selected_house = house
    # check if bottomleft, bottomright, topleft and top right of house overlap water
    if water.bottem_left[0] <= bottem_left[0] <= water.bottem_right[0] and water.top_left[1] <= bottom_left[1] <= water.bottem_left[1]:   
        break
        
    if water.bottem_left[0] <= bottem_right[0] <= water.bottem_right[0] and water.top_left[1] <= bottom_right[1] <= water.bottem_left[1]:   
        break
    
    if water.bottem_left[0] <= top_left[0] <= water.bottem_right[0] and water.top_left[1] <= top_left[1] <= water.bottem_left[1]:   
        break
    
    if water.bottem_left[0] <= top_right[0] <= water.bottem_right[0] and water.top_left[1] <= top_right[1] <= water.bottem_left[1]:   
        break

    # check if given cordinates overlap houses/obligated space
    for house in houses:
        # add obligated space with surface of house
        if house.size == "small":
            houseandgarden_bottom_left[0] += 2
            houseandgarden_bottom_right -= 2
            houseandgarden_bottom_right[0] += 2
            houseandgarden_top_left[1] += 2

            if houseandgarden_bottem_left[0] <= bottem_left[0] <= houseandgarden_bottom_right[1] and
            houseandgarden.top_left[1] <= bottom_left[1] <= houseandgarden.bottem_left[1]:
                pass
        
        if house.size == "medium":
            bottom_left[0] - 3
            bottem_left[1] + 3
        if house.size == "large":
            bottom_left[0] - 6
            bottem_left[1] + 6

    for small_house in number_small:
        small_house = House()

    for medium_house in number_medium

    def randomizer():
        ''' Generates a random x and y value'''
        # Daniel wil seed later gebruiken, zorgt voor zelfde uitkomst okal random
        # Kiara eandgarden_wil math.floor verwijderen voor exacte cordinaten ipv grid
        random_x = math.floor(random()*maximum_height)
        random_y = math.floor(random()*maximum_width)
        return (random_x, random_y)

    def ratio_houses(number_of_houses):
        '''Determines number of houses per size house '''
        small = int(ratio_small * number_of_houses)
        medium = int(ratio_medium * number_of_houses)
        large = int(ratio_large * number_of_houses)
        
        return (number_small, number_medium, number_large)

    def create_house_object(house_size, house_sort):
        '''Creates all the objects for a particular house and returns a list'''
        list_of_objects = []

        if house_sort == "small":
            count = 0
            for i in range(house_size):
                name = "S" + count
                small_house = House(name=name, size=small, start_value=285.000, obligated_space=2, rate=0.03, length=8, width=8)
                list_of_objects.append(small)
                count += 1
        if house_sort == "medium":
            count = 0
            for i in range(house_size):
                name = "M" + count
                large = House(name=name, size=medium, start_value=399.000, obligated_space=3, rate=0.04, length=11, width=7)
                list_of_objects.append(medium)
                count += 1
        if house_sort == "large":
            count = 0
            for i in range(house_size):
                name = "L" + count
                large = House(name=name, size=large, start_value=610.000, obligated_space=6, rate=0.06, length=12, width=10)
                list_of_objects.append(large)
        return list_of_objects

    def nodes_creator(house_sort)
    
        for house_nodes in list_of_objects:
            count = 0
            if house_sort == small:
                bottem_left1 = bottem_left
                bottem_left2 = bottem_left
                
                for i in range(width_length_small_house):
                    bottem_left1[1] + i = "node" + count
                for i in range(width_length_small_house):
                    bottem_left1[0] + i = "node" + count
                for i in range(width_length_small_house):
                    bottem_left2[1] + i = "node" + count



    def write_solution():
        # if file does not exist create
        # if file exists, open
        # write down number of the solution
        # if total_value map higher than last solution, delete all info last solution except total_value and picture
        # for house in solution write name, coordinates, total_value, extra space per house, save picture graph
        # write total of total_value map
        # else write total_value of map
        # close file
        pass

    def save_picture():
        # saves picture of graph
        pass
    
    def read_water_files(file):
        pass
                
    #vis.visualise(test_graph, 'data lalalla jason file)
    
                
            
        

if __name__ == "__main__":
    main()


