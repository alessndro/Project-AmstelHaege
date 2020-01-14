from models import House, Water
from random import seed
from random import random
from pilot import visualisation
import _random
import math
import csv

# Import the necessary packages and modules for matplotlib
import matplotlib.pyplot as plt
import numpy as np

#constants
RATIO_SMALL = 0.6
RATIO_MEDIUM = 0.25
RATIO_LARGE = 0.15
MAXIMUM_HEIGHT = 180
MAXIMUM_WIDTH = 160
WIDTH_LENGTH_SMALL_HOUSE = 8

def main():
    
    
    # ask user for number of houses to be placed
    while True:
        number_of_houses = int(input("What are the amount of Houses 20, 40 or 60?"))

        map_number = int(input("Which map would you like to use? 1,2,3"))
        
        if (number_of_houses == 20 or number_of_houses == 40 or number_of_houses == 60) and (map_number > 0 and map_number <= 3):
            break

    # determine division houses
    number_small, number_medium, number_large = ratio_houses(number_of_houses)

    # create list of objects
    small_houses = create_house_object(number_small, "small")
    medium_houses = create_house_object(number_medium, "medium")
    large_houses = create_house_object(number_large, "large")
    waters = create_water_object(map_number)
    
    # save lists in dictionary
    all_houses = {}
    all_houses["small"] = small_houses
    all_houses["medium"] = medium_houses
    all_houses["large"] = large_houses

    # plaats alle huizen
    for item in all_houses.values():
        for house in item:
            algoritme(house, all_houses, waters)
        
    # bereken alle afstanden tot alle huizen
    for item in all_houses.values():
        for house in item:
            bereken(house, all_houses)

    total_value_map = 0
    for item in all_houses.values():
        for house in item:
            house.extra_meters()
            total_value_map += house.totalprice()

    visualisation(all_houses=all_houses, waters=waters)

    print(total_value_map)
        

def algoritme(house, all_houses, waters):

    while True:

        while True:
            # returns a tuple of a cordinate x,y bottom left of house
            bottom_left = randomizer()

            # check if bottom left, bottom right, top left and top right of house inside map
            
            if bottom_left[0] < MAXIMUM_WIDTH - house.width and bottom_left[1] < MAXIMUM_HEIGHT - house.length:
                house.location(bottom_left)
                break
        
        
        # Check of het huis geplaatst kan worden
        if place_house(house, all_houses, waters) == True:
            # als huis geplaatst mag worden, plaats huis
            house.placed = True
            break


def place_house(selected_house, all_houses, waters):
    '''Bepaald of een huis op de gekozen locatie geplaatst kan worden '''
    # check if bottom left, bottom right, top left and top right of house overlap water
    
    for water in waters:
        if water.bottom_left[0] <= selected_house.bottom_left[0] <= water.bottom_right[0] and water.bottom_left[1] <= selected_house.bottom_left[1] <= water.top_left[1]:   
            return False
        
        if water.bottom_left[0] <= selected_house.bottom_right[0] <= water.bottom_right[0] and water.bottom_left[1] <= selected_house.bottom_right[1] <= water.top_left[1]:   
            return False

        if water.bottom_left[0] <= selected_house.top_left[0] <= water.bottom_right[0] and water.bottom_left[1] <= selected_house.top_left[1] <= water.top_left[1]:   
            return False

        if water.bottom_left[0] <= selected_house.top_right[0] <= water.bottom_right[0] and water.bottom_left[1] <= selected_house.top_right[1] <= water.top_left[1]:   
            return False


    # check if bottom left, bottom right, top left and top right of house inside map
    for item in all_houses.values():
        for houseplaced in item:
             # check if given cordinates of new house overlaps with houses and obligated space
            if houseplaced.placed == True and selected_house != houseplaced:

                # add obligated space with surface of house dependant on size
                selected_house_with_garden_bottom_left = ((selected_house.bottom_left[0] - selected_house.obligated_space),(selected_house.bottom_left[1] - selected_house.obligated_space))
                selected_house_with_garden_bottom_right = ((selected_house.bottom_right[0] + selected_house.obligated_space),(selected_house.bottom_right[1] - selected_house.obligated_space))
                selected_house_with_garden_top_right = ((selected_house.top_right[0] + selected_house.obligated_space),(selected_house.top_right[1] + selected_house.obligated_space))
                selected_house_with_garden_top_left = ((selected_house.top_left[0] - selected_house.obligated_space),(selected_house.top_left[1] + selected_house.obligated_space))

                # add obligated space with surface of house dependant on size
                # calculate bottom left of house and obligatory space/garden
                placed_house_with_garden_bottom_left = ((houseplaced.bottom_left[0] - houseplaced.obligated_space),(houseplaced.bottom_left[1] - houseplaced.obligated_space))
                # calculate bottom right of house and obligatory space/garden
                placed_house_with_garden_bottom_right = ((houseplaced.bottom_right[0] + houseplaced.obligated_space),(houseplaced.bottom_right[1] - houseplaced.obligated_space))
                # calculate top left of house and obligatory space/garden
                placed_house_with_garden_top_left = ((houseplaced.top_left[0] - houseplaced.obligated_space),(houseplaced.top_left[1] + houseplaced.obligated_space))
                
                # check whether both x and y cordinates of all four corners of new house not inside already placed house and garden
                # links bottom

                if (placed_house_with_garden_bottom_left[0] < selected_house_with_garden_bottom_left[0]) and (placed_house_with_garden_bottom_right[0] > selected_house_with_garden_bottom_left[0]) and (placed_house_with_garden_top_left[1] > selected_house_with_garden_bottom_left[1]) and (placed_house_with_garden_bottom_left[1] < selected_house_with_garden_bottom_left[1]):
                    return False
                # rechts bottom
                if (placed_house_with_garden_bottom_left[0] < selected_house_with_garden_bottom_right[0]) and (placed_house_with_garden_bottom_right[0] > selected_house_with_garden_bottom_right[0]) and (placed_house_with_garden_top_left[1] > selected_house_with_garden_bottom_right[1]) and (placed_house_with_garden_bottom_left[1] < selected_house_with_garden_bottom_right[1]):
                    return False

                if (placed_house_with_garden_bottom_left[0] < selected_house_with_garden_top_left[0]) and (placed_house_with_garden_bottom_right[0] > selected_house_with_garden_top_left[0]) and (placed_house_with_garden_top_left[1] > selected_house_with_garden_top_left[1]) and (placed_house_with_garden_bottom_left[1] < selected_house_with_garden_top_left[1]):
                    return False

                if (placed_house_with_garden_bottom_left[0] < selected_house_with_garden_top_right[0]) and (placed_house_with_garden_bottom_right[0] > selected_house_with_garden_top_right[0]) and (placed_house_with_garden_top_left[1] > selected_house_with_garden_top_right[1]) and (placed_house_with_garden_bottom_left[1] < selected_house_with_garden_top_right[1]):
                    return False


                if (placed_house_with_garden_bottom_left[0]] < selected_house_with_garden_bottom_left[0] < placed_house_with_garden_bottom_right[0]) and (placed_house_with_garden_bottom_left[1] < selected_house_with_garden_bottom_left[1] < placed_house_with_garden_top_left[1]):   
                    return False
        
                if (placed_house_with_garden_bottom_left[0] < selected_house_with_garden_bottom_right[0] < placed_house_with_garden_bottom_right[0]) and (placed_house_with_garden_bottom_left[1] < selected_house_with_garden_bottom_right[1] < placed_house_with_garden_top_left[1]):   
                    return False

                if (placed_house_with_garden_bottom_left[0] < selected_house_with_garden_top_left[0] < placed_house_with_garden_bottom_right[0]) and (placed_house_with_garden_bottom_left[1] < selected_house_with_garden_top_left[1] < placed_house_with_garden_top_left[1]):   
                    return False

                if (placed_house_with_garden_bottom_left[0] < selected_house_with_garden_top_right[0] < placed_house_with_garden_bottom_right[0]) and (placed_house_with_garden_bottom_left[1] < selected_house_with_garden_top_right[1] < placed_house_with_garden_top_left[1]):   
                    return False

            return True

def randomizer():
    ''' Generates a random x and y value'''
    # Daniel wil seed later gebruiken, zorgt voor zelfde uitkomst okal random
    # Kiara eandgarden_wil math.floor verwijderen voor exacte cordinaten ipv grid
    random_x = math.floor(random()*MAXIMUM_HEIGHT)
    random_y = math.floor(random()*MAXIMUM_WIDTH)
    return (random_x, random_y)

def ratio_houses(number_of_houses):
    '''Determines number of houses per size house '''
    small = int(RATIO_SMALL * number_of_houses)
    medium = int(RATIO_MEDIUM * number_of_houses)
    large = int(RATIO_LARGE * number_of_houses)
    
    return (small, medium, large)

def create_house_object(house_size, house_sort):
    '''Creates all the objects for a particular house and returns a list'''
    list_of_objects = []

    if house_sort == "small":
        count = 0
        for i in range(house_size):
            name = "S" + str(count)
            small = House(name=name, size=house_sort, start_value=285.000, obligated_space=2, rate=0.03, length=8, width=8)
            list_of_objects.append(small)
            count += 1
    if house_sort == "medium":
        count = 0
        for i in range(house_size):
            name = "M" + str(count)
            medium = House(name=name, size=house_sort, start_value=399.000, obligated_space=3, rate=0.04, length=11, width=7)
            list_of_objects.append(medium)
            count += 1
    if house_sort == "large":
        count = 0
        for i in range(house_size):
            name = "L" + str(count)
            large = House(name=name, size=house_sort, start_value=610.000, obligated_space=6, rate=0.06, length=12, width=10)
            list_of_objects.append(large)
            count += 1
    return list_of_objects

def create_water_object(map_number):
    print("DIT IS MAP NUMMER", map_number)
    print(type(map_number))
    waters = []
    if map_number == 1:
        print("HIER BEN IK")
        water = Water(map=1, top_right=(32,180), top_left=(0,180), bottom_right=(32,0), bottom_left=(0,0))
        waters.append(water)
    elif map_number == 2:
        water = Water(map=2, top_right=(135,180), top_left=(0,180), bottom_right=(135,128), bottom_left=(0,128))
        waters.append(water)
        water = Water(map=2, top_right=(160,180), top_left=(135,128), bottom_right=(160,128), bottom_left=(135,128))
        waters.append(water)
        water = Water(map=2, top_right=(32,55), top_left=(0,55), bottom_right=(32,0), bottom_left=(0,0))
        waters.append(water)
        water = Water(map=2, top_right=(160,32), top_left=(135,32), bottom_right=(160,0), bottom_left=(135,0))
        waters.append(water)
    elif map_number == 3:
        water0 = Water(map=3, top_right=(116,130), top_left=(44,130), bottom_right=(116,50), bottom_left=(44,50))
        waters.append(water0)

    print(waters)
    return waters

def bereken(selected_house, placed_houses):

    count = 0
    counter_statement = 0

    for item in placed_houses.values():
        for placed_house in item:

            if selected_house != placed_house:
                
                # links op de x-as
                if placed_house.bottom_right[0] <= selected_house.top_left[0]: 
                    # linksboven
                    if placed_house.bottom_right[1] >= selected_house.top_left[1]:
                        delta_x_sq = (selected_house.top_left[0]-placed_house.bottom_right[0])**(2)
                        delta_y_sq = (placed_house.bottom_right[1]-selected_house.top_left[1])**(2)
                        distance = math.sqrt(delta_x_sq + delta_y_sq)
                    # links onder
                    elif placed_house.top_right[1] <= selected_house.bottom_left[1]:
                        delta_x_sq = (selected_house.top_left[0]-placed_house.bottom_right[0])**(2)
                        delta_y_sq = (selected_house.bottom_left[1] - placed_house.top_right[1])**(2)
                        distance = math.sqrt(delta_x_sq + delta_y_sq)
                    # linksmidden
                    else:
                        distance = selected_house.bottom_left[0] - placed_house.bottom_right[0]
                        

                # rechts op de x-as
                elif placed_house.bottom_left[0] >= selected_house.top_right[0]:
                    # rechtsboven
                    if placed_house.bottom_left[1] >= selected_house.top_right[1]:
                        delta_x_sq = (placed_house.bottom_left[0]-selected_house.top_right[0])**(2)
                        delta_y_sq = (placed_house.bottom_left[1]-selected_house.top_right[1])**(2)
                        distance = math.sqrt(delta_x_sq + delta_y_sq)

                    # rechtsonder
                    elif placed_house.top_left[1] <= selected_house.bottom_right[1]:
                        delta_x_sq = (placed_house.top_left[0]-selected_house.bottom_right[0])**(2)
                        delta_y_sq = (selected_house.bottom_right[1]-placed_house.top_left[1])**(2)
                        distance = math.sqrt(delta_x_sq + delta_y_sq)
                    # rechtsmidden
                    else:
                        distance = placed_house.top_left[0] - selected_house.top_right[0]
                        
                # BOVEN OF ONDER
                else:
                    # boven
                    if placed_house.bottom_left[1] >= selected_house.top_left[1]:
                        distance = placed_house.bottom_left[1] - selected_house.top_left[1]
                    # onder
                    else:
                        distance = selected_house.bottom_left[1] - placed_house.top_left[1]

                if distance < 0:
                    print("NEGATIEF", selected_house, placed_house)
                selected_house.compared_space(placed_house, distance)

                

if __name__ == "__main__":
    main()