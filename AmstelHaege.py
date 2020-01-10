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
        number_of_houses = int(input("What are the amount of Houses 20, 40 or 60?"))

        if number_of_houses == 20 or number_of_houses == 40 or number_of_houses == 60:
            break

    # determine division houses
    number_small, number_medium, number_large = ratio_houses(number_of_houses)

    # create list of objects
    small_houses = create_house_object(number_small, "small")
    medium_houses = create_house_object(number_medium, "medium")
    large_houses = create_house_object(number_large, "large")
    
    # save lists in dictionary
    # all_houses = {}
    all_houses[small] = small_houses
    all_houses[medium] = medium_houses
    all_houses[large] = large_houses

    # plaats alle huizen
    for house in all_houses.values():
        algoritme(house)
        
    # bereken alle afstanden tot alle huizen
    for house in all_houses.values():
        bereken(house)


def algoritme(house):

    while True:

        # returns a tuple of a cordinate x,y bottom left of house
        bottom_left = randomizer()
        house.location(bottom_left)

        # Check of het huis geplaatst kan worden
        if place_house(house) == True:
            # als huis geplaatst mag worden, plaats huis
            house.placed = True
            break


def place_house(selected_house):
    '''Bepaald of een huis op de gekozen locatie geplaatst kan worden '''
    selected_house = house
    # check if bottom left, bottom right, top left and top right of house overlap water
    if water.bottom_left[0] <= house.bottom_left[0] <= water.bottom_right[0] and water.top_left[1] <= house.bottom_left[1] <= water.bottom_left[1]:   
        return False
        
    if water.bottom_left[0] <= house.bottom_right[0] <= water.bottom_right[0] and water.top_left[1] <= house.bottom_right[1] <= water.bottom_left[1]:   
        return False

    if water.bottom_left[0] <= house.top_left[0] <= water.bottom_right[0] and water.top_left[1] <= house.top_left[1] <= water.bottom_left[1]:   
        return False

    if water.bottom_left[0] <= house.top_right[0] <= water.bottom_right[0] and water.top_left[1] <= house.top_right[1] <= water.bottom_left[1]:   
        return False

    # check if given cordinates of new house overlaps with houses and obligated space
    for houseplaced in houses.placed == "yes":
        # add obligated space with surface of house dependant on size
        if house.size == "small":
            # calculate bottom left of house and obligatory space/garden
            houseandgarden_bottom_left[0] = houseplaced.bottom_left[0] - 2
            houseandgarden_bottom_left[1] = houseplaced.bottom_left[1] - 2
            # calculate bottom right of house and obligatory space/garden
            houseandgarden_bottom_right[0] = housplaced.bottom_right[0] + 2
            houseandgarden_bottom_right[1] = houseplaced.bottom_right[1] - 2
            # calculate top left of house and obligatory space/garden
            houseandgarden_top_left[0] = houseplaced.top_left[0] - 2
            houseandgarden_top_left[1] = houseplaced.top_left[1] + 2
            
            # check whether both x and y cordinates of all four corners of new house not inside already placed house and garden
            if houseandgarden_bottom_left[0] <= house.bottom_left[0] <= houseandgarden_bottom_right[0] and houseandgarden.top_left[1] <= house.bottom_left[1] <= houseandgarden.bottom_left[1]:
                return False
            if houseandgarden_bottom_left[0]  <= house.bottom_right[0] <= houseandgarden_bottom_right[0] and houseandgarden.top_left[1] <= house.bottom_right[1] <= houseandgarden.bottom_left[1]:   
                return False
            if houseandgarden_bottom_left[0]  <= house.top_left[0] <= houseandgarden_bottom_right[0] and houseandgarden.top_left[1] <= house.top_left[1] <= houseandgarden.bottom_left[1]:   
                return False
            if houseandgarden_bottom_left[0]  <= house.top_right[0] <= houseandgarden_bottom_right[0] and houseandgarden.top_left[1] <= house.top_right[1] <= houseandgarden.bottom_left[1]:   
                return False
        
        if house.size == "medium":
            # calculate bottom left of house and obligatory space/garden
            houseandgarden_bottom_left[0] = houseplaced.bottom_left[0] - 3
            houseandgarden_bottom_left[1] = houseplaced.bottom_left[1] - 3
            # calculate bottom right of house and obligatory space/garden
            houseandgarden_bottom_right[0] = houseplaced.bottom_right[0] + 3
            houseandgarden_bottom_right[1] = houseplaced.bottom_right[1] - 3
            # calculate top left of house and obligatory space/garden
            houseandgarden_top_left[0] = houseplaced.top_left[0] - 3
            houseandgarden_top_left[1] = houseplaced.top_left[1] + 3

            # check whether both x and y cordinates of all four corners of new house not inside already placed house and garden
            if houseandgarden_bottom_left[0] <= house.bottom_left[0] <= houseandgarden_bottom_right[0] and houseandgarden.top_left[1] <= house.bottom_left[1] <= houseandgarden.bottom_left[1]:
                return False

            if houseandgarden_bottom_left[0]  <= house.bottom_right[0] <= houseandgarden_bottom_right[0] and houseandgarden.top_left[1] <= house.bottom_right[1] <= houseandgarden.bottom_left[1]:   
                return False

            if houseandgarden_bottom_left[0]  <= house.top_left[0] <= houseandgarden_bottom_right[0] and houseandgarden.top_left[1] <= house.top_left[1] <= houseandgarden.bottom_left[1]:   
                return False

            if houseandgarden_bottom_left[0]  <= house.top_right[0] <= houseandgarden_bottom_right[0] and houseandgarden.top_left[1] <= house.top_right[1] <= houseandgarden.bottom_left[1]:   
                return False

        if house.size == "large":
            # bottom left of house and obligatory space/garden
            houseandgarden_bottom_left[0] = houseplaced.bottom_left[0] - 6
            houseandgarden_bottom_left[1] = houseplaced.bottom_left[1] - 6
            # bottom right of house and obligatory space/garden
            houseandgarden_bottom_right[0] = houseplaced.bottom_right[0] + 6
            houseandgarden_bottom_right[1] = houseplaced.bottom_right[1] - 6
            # top left of house and obligatory space/garden
            houseandgarden_top_left[0] = houseplaced.top_left[0] - 6
            houseandgarden_top_left[1] = houseplaced.top_left[1] + 6
        
            # check whether both x and y cordinates of all four corners of new house not inside already placed house and garden
            if houseandgarden_bottom_left[0] <= house.bottom_left[0] <= houseandgarden_bottom_right[0] and houseandgarden.top_left[1] <= house.bottom_left[1] <= houseandgarden.bottom_left[1]:
                return False

            if houseandgarden_bottom_left[0]  <= house.bottom_right[0] <= houseandgarden_bottom_right[0] and houseandgarden.top_left[1] <= house.bottom_right[1] <= houseandgarden.bottom_left[1]:   
                return False

            if houseandgarden_bottom_left[0]  <= house.top_left[0] <= houseandgarden_bottom_right[0] and houseandgarden.top_left[1] <= house.top_left[1] <= houseandgarden.bottom_left[1]:   
                return False

            if houseandgarden_bottom_left[0]  <= house.top_right[0] <= houseandgarden_bottom_right[0] and houseandgarden.top_left[1] <= house.top_right[1] <= houseandgarden.bottom_left[1]:   
                return False

    return True

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

# # vul object huis in met bottom_left coordinaten
# def fill_information_house(bottom_left, house):
#     '''Vult alle coordinaten in van het object op basis van het random punt dat is gekozen ''' 
#     if house_size == small:
#         count = 0
#         for i in range(8):
#             for j in range(8):
#                 bottom_left(: + i ,: + j) = "s" + count
#                 count += 1

def bereken(selected_house, placed_houses):

    for placed_house in placed_houses:
        
        if selected_house != placed_house:
            # onder
            if placed_house.bottom_left[1] <= selected_house.bottom_left[1] and (selected_house.top_left[0] <= placed_house.bottom_left[0] <= selected_house.top_right[0] or selected_house.top_left[0] <= placed_house.bottom_right[0] <= selected_house.top_right[0]):
                distance = selected_house.bottom_left[1] - placed_house.top_left[1]
            # boven
            if placed_house.bottom_right[1] >=  selected_house[1] and (selected_house.bottom_left[0] <= placed_house.bottom_right[0] <= selected_house.top_left[0] or selected_house.bottom_left[0] <= placed_house.bottem_left[0] <= selected_house.top_left[0]):
                distance = placed_house.bottom_right[1]-selected_house.top_right[1]
            
            #links
            if placed_house.bottom_right[0] <= selected_house.bottom_right[0] and (selected_house.bottom_left[1] <= placed_house.bottom_right[1] <= selected_house.top_left[1] or selected_house.bottom_left[1] <= placed_house.top_right[1] <= selected_house.top_left[1]):
                distance = selected_house.bottom_left[0]-placed_house.bottom_right[0]

            #rechts
            if placed_house.bottom_right[0] >= selected_house.bottom_left[0] and (selected_house.bottom_left[1] <= placed_house.bottom_right[1] <= selected_house.top_left[1] or selected_house.bottom_left[1] <= placed_house.top_right[1] <= selected_house.top_left[1]):
                distance = placed_house.bottom_right[0] - selected_house.bottom_left[0]

            # linksboven
            if selected_house.bottom_right[0] < placed_house.top_left [0] and selected_house.bottom_right[1] > placed_house.top_left[1]:
                # gebruik right bottom other placed house and top left placed house]
                distance = math.sqrt((selected_house.bottom_right[0]-placed_house.bottom_right[0])**(2))+((selected_house.bottom_right[1]-placed_house.top_left[1])**(2))

            # rechtsboven
            if selected_house.bottom_left[0] > placed_house.top_right[0] and selected_house.bottom_left[1] > placed_house.top_right[1]:
                # gebruik left bottom other placed house and top right placed house
                distance = math.sqrt((selected_house.bottom_left[0]-placed_house.top_right[0])**(2))+((selected_house.bottom_right[1]-placed_house.top_left[1])**(2))

            # rechtsonder
            if selected_house.top_left[0] > placed_house.bottom_right[0] and selected_house.top_left[1] < placed_house.bottom_right[1]:
                # gebruik top left other placed house and bottom right placed house
                distance = math.sqrt((placed_house.bottom_left[0]-selected_house.top_right[0])**(2))+((placed_house.bottom_left[1]-selected_house.top_right[1])**(2))

            # linksonder
            if selected_house.top_right[0] < placed_house.bottom_left[0] and selected_house.top_right[1] < placed_house.bottom_left[1]:
                # gebruik top right other placed house and bottom left placed house
                distance = math.sqrt((selected_house.top_left[0]-placed_house.bottom_right[0])**(2))+((placed_house.bottom_right[1]-selected_house.top_left[1])**(2))


def write_solution():
    pass