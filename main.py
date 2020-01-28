#########################################################################
# main.py
#
# Minor Programming 
#
# Kiara Evers, Alessandro Degenkamp, Daniel Siha
#
# Bevat hoofdfile om het probleem Amstel-Haege met algoritmes op te lossen
##########################################################################

from code.classes.models import House, Water
from code.visualisation import visualisation, visualisation_plot
from code.writer import *
from code.algorithms.hf import *
import copy
import time
from random import seed, random

# importen van alle benodigde algoritmes
from code.algorithms.random import *
from code.algorithms.ascending_hillclimber import *
from code.algorithms.greedy import *
from code.algorithms.swapping_houses import *
from code.algorithms.random_points_ascending_hillclimber import *
from code.algorithms.greedy_swap_turn import *

# importen van benodigde pakketten voor de visualisatie
import matplotlib.pyplot as plt
import numpy as np

# constanten
RATIO_SMALL = 0.6
RATIO_MEDIUM = 0.25
RATIO_LARGE = 0.15
MAXIMUM_HEIGHT = 180
MAXIMUM_WIDTH = 160
WIDTH_LENGTH_SMALL_HOUSE = 8

def main():

    while True:

        number_of_houses, map_number, algoritme = get_input()

        # initialiseer de variabelen die benodigd zijn voor het runnen
        all_houses_dic = {}
        all_houses = {}
        total_value_map = 0
        total_value = 0
        waters = []
        count = 0

        # RANDOM
        if algoritme == 1:
            while True:
                turns = int(input("Uit hoeveel keer wil je dat er een random gemaakt wordt? Enkel de gene met de hoogste waarde wordt weergeven. \n"))
                if turns > 0:
                    break
            total_value, all_houses_dic, waters = random_start(number_of_houses=number_of_houses, map_number=map_number, turns=turns)

        # bepaalde de totale run-time van het programma
        t = time.time()
        elap = time.time() - t

        # ASCENDING HILLCLIMBER
        if algoritme == 2:
            total_value, all_houses_dic, waters = asceding_hillclimber_algoritme(number_of_houses=number_of_houses,
            map_number=map_number, all_houses=all_houses, waters = waters, total_value_map=total_value_map)

        # VOOR GREEDY
        if algoritme == 3:
            total_value, all_houses_dic, waters = greedy(number_of_houses=number_of_houses,
            map_number=map_number, waters=waters, total_value_map=total_value_map)

        # VOOR SWAPPING HOUSES
        if algoritme == 4:    
            total_value, all_houses_dic, waters = swapping_houses_algoritme(number_of_houses=number_of_houses,
            map_number=map_number, all_houses=all_houses, waters=waters, total_value_map=total_value_map, algoritme=algoritme)

        # VOOR DOUBLE RANDOM 
        if algoritme == 5:
            total_value, all_houses_dic, waters = random_points_ascending_hillclimber_algoritme(number_of_houses=number_of_houses, map_number=map_number)

        # SWAP HOUSES NA GREEDY
        if algoritme == 6:
            total_value, all_houses_dic, waters = swap_houses_after_greedy_algoritme(number_of_houses=number_of_houses, map_number=map_number,
            waters=waters, total_value_map=total_value_map, algoritme=algoritme)
        
        # noteert de resultaten
        write_progress(number_of_houses=number_of_houses, map_number=map_number, total_value_map=total_value, all_houses=all_houses_dic)
        if algoritme != 1:
            write_progress_run(number_of_houses=number_of_houses, map_number=map_number, total_value_map=total_value)

        
        elap = time.time() - t
        # visualisatie 
        visualisation(all_houses=all_houses_dic, waters=waters) 
        visualisation_plot(algoritme)

        delete_progress_run()

        # toont het resultaat van het programma
        print("TOTAL VALUE MAP: ",total_value)
        print("RUN TIME: ", elap)

        beeindigen = int(input("Om het programma opnieuw te runnen toets 1, indien u niet verder gaat met het programma" + 
                            " wordt process_run.csv geleegd. Wanneer u wel verder gaat wordt deze verder aangevuld. \n"))
        if beeindigen != 1:
            delete_progress_run()
            break
        
if __name__ == "__main__":
    main()


