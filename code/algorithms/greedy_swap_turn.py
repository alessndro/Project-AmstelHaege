#########################################################################
# greedy_swap_turn.py
#
# Minor Programming 
#
# Kiara Evers, Alessandro Degenkamp, Daniel Siha
#
# Bevat optie eerst greedy algoritme en swapping houses inclusief draaien
##########################################################################
from .hf import *
from .greedy import greedy_algoritme
from .swapping_houses import swap_houses
import copy

def swap_houses_after_greedy_algoritme(number_of_houses, map_number, waters, total_value_map, algoritme):
    '''Maakt gebruikt van het greedy algoritme, swapt vervolgens de huizen met het swapping algoritme, 
       en bij de laatste keer maakt deze gebruikt van het swapping algoritme om de huizen een kwartslag
       te draaien en te kijken of deze geplaatst kan worden en of dit vervolgens dan ook de totale waarde
       van de kaart verhoogt'''

    # bepaal de verdeling van de huizen
    number_small, number_medium, number_large = ratio_houses(number_of_houses)

    # creeert lijsten met objecten van de juiste grootte
    small_houses = create_house_object(number_small, "small")
    medium_houses = create_house_object(number_medium, "medium")
    large_houses = create_house_object(number_large, "large")
    waters = create_water_object(map_number)

    all_houses_dic = {}
    # slaat de lijsten op in de dictionairy
    all_houses_dic["small"] = small_houses
    all_houses_dic["medium"] = medium_houses
    all_houses_dic["large"] = large_houses

    # loop door alle huizen en plaats deze op de meest gunstige plek volgens het greedy algoritme
    for house in all_houses_dic["large"]:
        all_houses_dic, total_value = greedy_algoritme(house, all_houses_dic, waters)

    for house in all_houses_dic["medium"]:
        all_houses_dic, total_value = greedy_algoritme(house, all_houses_dic, waters)

    for house in all_houses_dic["small"]:
        all_houses_dic, total_value = greedy_algoritme(house, all_houses_dic, waters)

    # swap de huizen om een hogere totale waarde te krijgen
    for item in all_houses_dic.values():
        for house in item:
            all_houses_new, total_value = swap_houses(house=house, all_houses=all_houses_dic,
                                                    waters=waters, total_value_map=total_value, algoritme=0)

    for item in all_houses_new.values():
        for house in item:
            all_houses, total_value = swap_houses(house=house, all_houses=all_houses_dic,
                                                 waters=waters, total_value_map=total_value, algoritme=algoritme)
        
    all_houses_dic = copy.deepcopy(all_houses)

    return total_value, all_houses_dic, waters