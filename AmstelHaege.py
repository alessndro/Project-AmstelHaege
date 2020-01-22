from models import House, Water
from random import seed
from random import random
from visualisation import visualisation, visualisation_plot
from writer import write_progress, write_progress_run
import _random
import math
import csv
import copy
import time

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

    t = time.time()
    #script zonder plot
    elap = time.time() - t

    # ask user for number of houses to be placed
    while True:
        number_of_houses = int(input("What are the amount of Houses 20, 40 or 60?"))

        map_number = int(input("Which map would you like to use? 1,2,3"))
        
        if (number_of_houses == 20 or number_of_houses == 40 or number_of_houses == 60) and (map_number > 0 and map_number <= 3):
            break

    all_houses_dic = {}
    total_value_map = 0
    waters = []
    count = 0
    #############################################################################
    # RANDOM 
    #############################################################################
    # for i in range(1):
    #     print(count)
    #     all_houses, total_value, waters = random_algoritme(number_of_houses, map_number)
    #     write_progress(number_of_houses=number_of_houses, map_number=map_number, solution=count, total_value_map=total_value)
    #     write_progress_run(number_of_houses=number_of_houses, map_number=map_number, solution=count, total_value_map=total_value)
    #     if total_value > total_value_map:
    #         total_value_map = total_value
    #         print(total_value)
    #         all_houses_dic = copy.deepcopy(all_houses)
    #     count += 1

    # visualisation(all_houses=all_houses, waters=waters)
    
    ##############################################################################
    # VOOR GREEDY
    ##############################################################################
    
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

    for house in all_houses["large"]:
        all_houses_new, total_value = greedy_algoritme(house, all_houses, waters)

        
    visualisation(all_houses=all_houses_new, waters=waters)            #!!!
    visualisation_plot()
    

    for house in all_houses["medium"]:
        all_houses_new, total_value = greedy_algoritme(house, all_houses, waters)

        
    visualisation(all_houses=all_houses_new, waters=waters)            #!!!
    visualisation_plot()

    for house in all_houses_new["small"]:
        all_houses_new, total_value = greedy_algoritme(house, all_houses, waters)
    


    ##################################################################################
    # loops for testing the different algoritms
    #################################################################################

    #for item in all_houses.values():
    #   for house in item:
    #          all_houses1, new_total=algoritme2(house=house,all_houses=all_houses, waters=waters, total_value_map=total_value_map)
    
    # print("tussendoor", new_total)

    #for item in all_houses1.values():
        #for house in item:
            #all_houses2, new_total=algoritme5(house=house,all_houses=all_houses1, waters=waters, total_value_map=total_value_map)

    # for item in all_houses2.values():
    #     for house in item:
    #         all_houses3, new_total=algoritme2(house=house,all_houses=all_houses2, waters=waters, total_value_map=total_value_map)

    # for item in all_houses3.values():
    #     for house in item:
    #         all_houses4, new_total=algoritme2(house=house,all_houses=all_houses3, waters=waters, total_value_map=total_value_map)
    
    # for item in all_houses4.values():
    #     for house in item:
    #         all_houses5, new_total=algoritme2(house=house,all_houses=all_houses4, waters=waters, total_value_map=total_value_map)

    
    
    visualisation(all_houses=all_houses_new, waters=waters) 
    elap = time.time() - t
    visualisation_plot()
    print("HOOGSTE ", total_value)

def random_algoritme(number_of_houses, map_number):

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
    for house in all_houses["large"]:
        algoritme(house, all_houses, waters)

    for house in all_houses["medium"]:
        algoritme(house, all_houses, waters)

    for house in all_houses["small"]:
        algoritme(house, all_houses, waters)

    for items in all_houses.values():
        for selected_house in items:
            total_distance(selected_house, all_houses)

    total_value_map = 0
    for item in all_houses.values():
        for house in item:
            house.extra_meters()
            total_value_map += house.totalprice()

    return all_houses, total_value_map, waters

def algoritme(house, all_houses, waters):
    '''Places all houses at random locations '''

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
    
    
def algoritme2(house, all_houses, waters, total_value_map):
    ''' Ascending hillclimber plaatst huizen op een nieuwe locatie afhankelijk van totale waarde kaart '''
    total_value_map_NEW = total_value_map

    # check in welke range het huis geplaats kan worden, niet kijkend naar water of andere 
    rangex = MAXIMUM_WIDTH - house.length
    rangey = MAXIMUM_HEIGHT - house.width
    # iterate over all cordinates
    for x in range(rangex):
        for y in range(rangey):
            if house.placed == True:
                tempx = house.bottom_left[0]
                tempy = house.bottom_left[1]
                # save cordinates house.bottom_left
                bottom_left = (x,y)
                # change cordinates of bl to new location
                house.location(bottom_left)
                # if you can place house on new location

                if place_house(house, all_houses, waters) == True:
                    # bereken nieuw waarde map, waarin huis is verplaatst
                    total_value_map_temp = 0
                    for item in all_houses.values():
                        for house in item:
                            house.extra_meters()
                            total_value_map_temp += house.totalprice()

                    # als waarde met nieuwe locatie hoger is, verander deze
                    if total_value_map_NEW < total_value_map_temp:
                        total_value_map_NEW = total_value_map_temp
                        
                    # als waarde niet hoger is verander naar oude locatie
                    else:
                        bottom_left = (tempx,tempy)
                        house.location(bottom_left)
                        if place_house(house, all_houses, waters) == True:
                            for item in all_houses.values():
                                for houses in item:
                                    houses.extra_meters()
                                    houses.totalprice()
                else:
                    bottom_left = (tempx,tempy)
                    house.location(bottom_left)
                    if place_house(house, all_houses, waters) == True:
                        for item in all_houses.values():
                            for houses in item:
                                houses.extra_meters()
                                houses.totalprice()
            
    return all_houses, total_value_map_NEW
    
    
def algoritme3(house, all_houses, waters, total_value_map):
    """pakt random 100 punten en kijkt of de totale waarde hoger wordt"""
    total_value_map_NEW = total_value_map

    # check in welke range het huis geplaats kan worden, niet kijkend naar water of andere 
    rangex = MAXIMUM_WIDTH - house.width
    rangey = MAXIMUM_HEIGHT - house.length

    for x in range(100):

        randomizex = 0 + rangex * random()
        randomizey = 0 + rangey * random()

        tempx = house.bottom_left[0]
        tempy = house.bottom_left[1]
        # save cordinates house.bottom_left
        bottom_left = (randomizex,randomizey)
        # change cordinates of bl to new location
        house.location(bottom_left)
        # if you can place house on new location
        if place_house(house, all_houses, waters) == True:
            # bereken nieuw waarde map, waarin huis is verplaatst
            total_value_map_temp = 0
            for item in all_houses.values():
                for house in item:
                    house.extra_meters()
                    total_value_map_temp += house.totalprice()

            # als waarde met nieuwe locatie hoger is, verander deze
            if total_value_map_NEW < total_value_map_temp:
                total_value_map_NEW = total_value_map_temp
            # als waarde niet hoger is verander naar oude locatie
            else:
                bottom_left = (tempx,tempy)
                house.location(bottom_left)
                if place_house(house, all_houses, waters) == True:
                    for item in all_houses.values():
                        for houses in item:
                            houses.extra_meters()
                            houses.totalprice()
        else:
            bottom_left = (tempx,tempy)
            house.location(bottom_left)
            if place_house(house, all_houses, waters) == True:
                    for item in all_houses.values():
                        for houses in item:
                            houses.extra_meters()
                            houses.totalprice()

    return all_houses, total_value_map_NEW


def algoritme4(house, all_houses, waters, total_value_map):
    total_value_map_NEW = total_value_map
     
    rangex = MAXIMUM_WIDTH - house.length
    rangey = MAXIMUM_HEIGHT - house.width
    
    for i in range(-5,5):
        for j in range(-5,5):

        
            checkx = house.bottom_left[0] + i
            checky = house.bottom_left[1] + j

            if checkx >= 0 and checky >= 0:
                if checkx <= rangex and checky <= rangey:

                    tempx = house.bottom_left[0]
                    tempy = house.bottom_left[1]
                    # save cordinates house.bottom_left
                    bottom_left = (checkx,checky)
                    # change cordinates of bl to new location
                    house.location(bottom_left)
                    # if you can place house on new location

                    if place_house(house, all_houses, waters) == True:
                        # bereken nieuw waarde map, waarin huis is verplaatst
                        total_value_map_temp = 0
                        for item in all_houses.values():
                            for house in item:
                                house.extra_meters()
                                total_value_map_temp += house.totalprice()

                        # als waarde met nieuwe locatie hoger is, verander deze
                        if total_value_map_NEW < total_value_map_temp:
                            total_value_map_NEW = total_value_map_temp
                        # als waarde niet hoger is verander naar oude locatie
                        else:
                            bottom_left = (tempx,tempy)
                            house.location(bottom_left)
                    else:
                        bottom_left = (tempx,tempy)
                        house.location(bottom_left)

    return all_houses, total_value_map_NEW

def algoritme5(house, all_houses, waters, total_value_map):
    """swapt huizen en kijkt of de totale waarde verandert"""
    total_value_map_NEW = total_value_map
    selected_house = house

    for item in all_houses.values():
        for placed_house in item:
            if placed_house != selected_house:
                # sla de oude locaties van de huizen op
                temp_selected_bl = selected_house.bottom_left
                
                temp_placed_bl = placed_house.bottom_left

                placed_house.location(temp_selected_bl)

                selected_house.location(temp_placed_bl)
                
                if place_house(selected_house, all_houses, waters) == True and place_house(placed_house, all_houses, waters) == True:                  
                    # bereken nieuw waarde map, waarin huis is verplaatst
                    total_value_map_temp = 0
                    for item in all_houses.values():
                        for house in item:
                            house.extra_meters()
                            total_value_map_temp += house.totalprice()

                    # als waarde met nieuwe locatie hoger is, verander deze
                    if total_value_map_NEW < total_value_map_temp:
                        total_value_map_NEW = total_value_map_temp
                    # als waarde niet hoger is verander naar oude locatie
                    else:
                        placed_house.location(temp_placed_bl)
                        selected_house.location(temp_selected_bl)
                        if place_house(selected_house, all_houses, waters) == True and place_house(placed_house, all_houses, waters) == True:
                            for item in all_houses.values():
                                for house in item:
                                    house.extra_meters()
                                    house.totalprice()
                    
                else:
                    placed_house.location(temp_placed_bl)
                    selected_house.location(temp_selected_bl)
                    if place_house(selected_house, all_houses, waters) == True and place_house(placed_house, all_houses, waters) == True:
                        for item in all_houses.values():
                            for house in item:
                                house.extra_meters()
                                house.totalprice()

    return all_houses, total_value_map_NEW
    

def greedy_algoritme(house, all_houses, waters):

    algoritme(house, all_houses, waters)
    house.extra_meters()
    house.totalprice()

    total_value_map_NEW = 0
    # check in welke range het huis geplaats kan worden, niet kijkend naar water of andere 
    rangex = MAXIMUM_WIDTH - house.length
    rangey = MAXIMUM_HEIGHT - house.width
    # iterate over all cordinates
    for x in range(rangex):
        for y in range(rangey):
            tempx = house.bottom_left[0]
            tempy = house.bottom_left[1]
            # save cordinates house.bottom_left
            bottom_left = (x,y)
            # change cordinates of bl to new location
            house.location(bottom_left)
            # if you can place house on new location
            print(place_house(house, all_houses, waters))
            if place_house(house, all_houses, waters) == True:
                # bereken nieuw waarde map, waarin huis is verplaatst
                total_value_map_temp = 0
                for item in all_houses.values():
                    for selected_house in item:
                        if selected_house.placed == True:
                            selected_house.extra_meters()
                            total_value_map_temp += selected_house.totalprice()

                # als waarde met nieuwe locatie hoger is, verander deze
                if total_value_map_NEW < total_value_map_temp:
                    total_value_map_NEW = total_value_map_temp
                    
                # als waarde niet hoger is verander naar oude locatie
                else:
                    bottom_left = (tempx,tempy)
                    house.location(bottom_left)
                    if place_house(house, all_houses, waters) == True:
                        for item in all_houses.values():
                            for houses in item:
                                houses.extra_meters()
                                houses.totalprice()
            else:
                bottom_left = (tempx,tempy)
                house.location(bottom_left)
                if place_house(house, all_houses, waters) == True:
                        for item in all_houses.values():
                            for houses in item:
                                houses.extra_meters()
                                houses.totalprice()
            
    return all_houses, total_value_map_NEW
    


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
    
if __name__ == "__main__":
    main()


