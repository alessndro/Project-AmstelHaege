from models import House, Water
from random import seed
from random import random
import math

#constants
RATIO_SMALL = 0.6
RATIO_MEDIUM = 0.25
RATIO_LARGE = 0.15
MAXIMUM_HEIGHT = 180
MAXIMUM_WIDTH = 160
WIDTH_LENGTH_SMALL_HOUSE = 8

def place_house(selected_house, all_houses, waters):
    '''Bepaald of een huis op de gekozen locate geplaatst kan worden '''

    for water in waters:
        distance = distance_berekening(selected_house, water)
        if distance <= 0:
            return False

        if water.bottom_left[0] <= selected_house.bottom_left[0] <= water.bottom_right[0] and water.bottom_left[1] <= selected_house.bottom_left[1] <= water.top_left[1]:   
            return False
        if water.bottom_left[0] <= selected_house.bottom_right[0] <= water.bottom_right[0] and water.bottom_right[1] <= selected_house.bottom_right[1] <= water.top_right[1]:   
            return False
        if water.bottom_left[0] <= selected_house.top_left[0] <= water.bottom_right[0] and water.bottom_left[1] <= selected_house.top_left[1] <= water.top_left[1]:   
            return False
        if water.bottom_left[0] <= selected_house.top_right[0] <= water.bottom_right[0] and water.bottom_right[1] <= selected_house.top_right[1] <= water.top_right[1]:   
            return False

    

    for key in all_houses.values():
        for placed_house in key:
            if (placed_house.placed == True) and (selected_house != placed_house):
                distance = distance_berekening(selected_house, placed_house)
                # HIER DE = NOG WEGHALEN LATER
                if distance <= placed_house.obligated_space or distance <= selected_house.obligated_space:
                    return False
                selected_house.compared_space(placed_house, distance)
                placed_house.compared_space(selected_house, distance)
    return True


def distance_berekening(selected_house, placed_house):

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

    return distance


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
            small = House(name=name, size=house_sort, start_value=285000, obligated_space=2, rate=0.03, length=8, width=8)
            list_of_objects.append(small)
            count += 1
    if house_sort == "medium":
        count = 0
        for i in range(house_size):
            name = "M" + str(count)
            medium = House(name=name, size=house_sort, start_value=399000, obligated_space=3, rate=0.04, length=7, width=11)
            list_of_objects.append(medium)
            count += 1
    if house_sort == "large":
        count = 0
        for i in range(house_size):
            name = "L" + str(count)
            large = House(name=name, size=house_sort, start_value=610000, obligated_space=6, rate=0.06, length=10, width=12)
            list_of_objects.append(large)
            count += 1
    return list_of_objects

def create_water_object(map_number):
    waters = []
    if map_number == 1:
        water = Water(map=1, top_right=(32,180), top_left=(0,180), bottom_right=(32,0), bottom_left=(0,0))
        waters.append(water)
    elif map_number == 2:
        water = Water(map=2, top_right=(32,55), top_left=(0,55), bottom_right=(32,0), bottom_left=(0,0))
        waters.append(water)
        water = Water(map=2, top_right=(160,32), top_left=(135,32), bottom_right=(160,0), bottom_left=(135,0))
        waters.append(water)
        water = Water(map=2, top_right=(45,180), top_left=(0,180), bottom_right=(45,128), bottom_left=(0,128))
        waters.append(water)
        water = Water(map=2, top_right=(160,180), top_left=(135,180), bottom_right=(160,128), bottom_left=(135,128))
        waters.append(water)
    elif map_number == 3:
        water0 = Water(map=3, top_right=(116,130), top_left=(44,130), bottom_right=(116,50), bottom_left=(44,50))
        waters.append(water0)

    return waters