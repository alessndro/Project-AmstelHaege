from models import House, Water
from random import seed
from random import random
from helpers_functions.py import place_house, distance_berekening, randomizer, ratio_houses, create_house_object, create_water_object
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

        algoritme = int(input("Which algorithm would you like to use?  press 1 for random algorithm, 2 for ascending hillclimber, 3 for greedy, 4 for swappinghouses"))
        
        if (number_of_houses == 20 or number_of_houses == 40 or number_of_houses == 60) and (map_number > 0 and map_number <= 3) and algoritme > 0 and algoritme < 5:
            break

    all_houses_dic = {}
    total_value_map = 0
    total_value = 0
    waters = []

    #############################################################################
    # RANDOM 
    #############################################################################
    if algoritme == 1:
        for i in range(1):
            print(count)
            all_houses_dic, total_value, waters = random_algoritme(number_of_houses, map_number)
            write_progress(number_of_houses=number_of_houses, map_number=map_number, solution=count, total_value_map=total_value)
            write_progress_run(number_of_houses=number_of_houses, map_number=map_number, solution=count, total_value_map=total_value)
            if total_value > total_value_map:
                total_value_map = total_value
                print(total_value)
                all_houses_dic = copy.deepcopy(all_houses) #!!! dit was eerst een andere variabel
            count += 1

    ##############################################################################
    # ASCENDING HILLCLIMBER
    ##############################################################################
    if algoritme == 2:
        for item in all_houses.values():
            for house in item:
                all_houses_dic, total_value = ascending_hillclimber(house=house, all_houses=all_houses, waters=waters, total_value_map=total_value_map)

    ##############################################################################
    # VOOR GREEDY
    ##############################################################################
    if algoritme == 3:
        # determine division houses
        number_small, number_medium, number_large = ratio_houses(number_of_houses)

        # create list of objects
        small_houses = create_house_object(number_small, "small")
        medium_houses = create_house_object(number_medium, "medium")
        large_houses = create_house_object(number_large, "large")
        waters = create_water_object(map_number)

        # save lists in dictionary
        all_houses["small"] = small_houses
        all_houses["medium"] = medium_houses
        all_houses["large"] = large_houses

        for house in all_houses["large"]:
            all_houses_dic, total_value = greedy_algoritme(house, all_houses, waters)

        for house in all_houses["medium"]:
            all_houses_dic, total_value = greedy_algoritme(house, all_houses_dic, waters)

        for house in all_houses["small"]:
            all_houses_dic, total_value = greedy_algoritme(house, all_houses_dic, waters)

    ################################################################################
    # VOOR SWAPPING HOUSES
    ################################################################################
    if algoritme == 4:

        for i in range(1):
            all_houses, total_value, waters = random_algoritme(number_of_houses, map_number)
            write_progress(number_of_houses=number_of_houses, map_number=map_number, solution=count, total_value_map=total_value)
            write_progress_run(number_of_houses=number_of_houses, map_number=map_number, solution=count, total_value_map=total_value)
            if total_value > total_value_map:
                total_value_map = total_value
                print(total_value)
                all_houses_dic = copy.deepcopy(all_houses)
            count += 1

    ##################################################################################
    # Visualisatie 
    ##################################################################################
    visualisation(all_houses=all_houses_dic, waters=waters) 
    elap = time.time() - t
    visualisation_plot()
    print (total_value)
    print(elap)
    
    
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
    
    
if __name__ == "__main__":
    main()


