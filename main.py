from models import House, Water
from helpers_functions import place_house, distance_berekening, randomizer, ratio_houses, create_house_object, create_water_object
from algorithms import random_algoritme, randomizer_algorithm, ascending_hillclimber, greedy_algoritme, swap_houses, random_ascending_hillclimber
from visualisation import visualisation, visualisation_plot
from writer import write_progress, write_progress_run
import math
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

    # bepaalde de totale run-time van het programma
    t = time.time()
    elap = time.time() - t

    number_of_houses, map_number, algoritme = get_input()

    # initialiseer de variabelen die benodigd zijn voor het runnen
    all_houses_dic = {}
    total_value_map = 0
    total_value = 0
    waters = []
    count = 0

    # RANDOM
    if algoritme == 1:
        total_value, all_houses_dic, waters = random(algoritme, number_of_houses, map_number, total_value_map)

    # ASCENDING HILLCLIMBER
    if algoritme == 2:
        total_value, all_houses_dic, waters = asceding_hillclimber_algoritme(number_of_houses=number_of_houses, map_number, all_houses=all_houses, waters = waters, total_value_map=total_value_map)

    # VOOR GREEDY
    if algoritme == 3:
        total_value, all_houses_dic, waters = greedy(number_of_houses=number_of_houses, map_number=map_number, all_houses=all_houses, waters=waters, total_value_map=total_value_map)

    # VOOR SWAPPING HOUSES
    if algoritme == 4:    
        total_value, all_houses_dic, waters = swapping_houses_algoritme(number_of_houses=number_of_houses, map_number=map_number, all_houses=all_houses, waters=waters, total_value_map=total_value_map)

    # VOOR DOUBLE RANDOM 
    if algoritme == 5:
        total_value, all_houses_dic, waters = random_ascending_hillclimber_algoritme(number_of_houses=number_of_houses, map_number=map_number, all_houses=all_houses, waters=waters, total_value_map=total_value_map)

    # SWAP HOUSES NA GREEDY
    if algoritme == 6:
        total_value, all_houses_dic, waters = swap_houses_after_greedy_algoritme(number_of_houses=number_of_houses, map_number=map_number, all_houses=all_houses, waters=waters, total_value_map=total_value_map, algoritme=algoritme)
        

    # Visualisatie 
    visualisation_map()
    
    visualisation(all_houses=all_houses_dic, waters=waters) 
    elap = time.time() - t
    visualisation_plot()
    print("TOTAL VALUE MAP: ",total_value)
    print("RUN TIME: ", elap)
    
    

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


