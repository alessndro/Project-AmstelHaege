#########################################################################
# swapping_houses.py
#
# Minor Programming 
#
# Kiara Evers, Alessandro Degenkamp, Daniel Siha
#
# Bevat het swap houses algoritme
##########################################################################
from .hf import *
from .random import random_algoritme
import copy

def swapping_houses_algoritme(number_of_houses, map_number, all_houses, waters, total_value_map, algoritme):
    ''' plaatst de huizen random, en swapt vervolgens de huizen met elkaar om te kijken of
        dit een hogere waarde zal opleveren (all_houses en waters worden meegegeven voor algoritme nummer 6) '''

    # plaatst de huizen random
    if algoritme == 4:
        all_houses, total_value, waters = random_algoritme(number_of_houses, map_number)

    # roept het algoritme aan voor het swappen van de huizen
    for item in all_houses.values():
        for house in item:
            all_houses_new, total_value = swap_houses(house=house, all_houses=all_houses, waters=waters, total_value_map=total_value_map, algoritme=algoritme)
        
        all_houses_dic = copy.deepcopy(all_houses_new)

    return total_value, all_houses_dic, waters

def swap_houses(house, all_houses, waters, total_value_map, algoritme):
    ''' Swapt huizen en kijkt of de totale waarde hoger wordt '''

    # initialiseer nieuwe totale waarde en geselecteerde huis
    total_value_map_NEW = total_value_map
    selected_house = house

    # loop door alle huizen
    for item in all_houses.values():
        for placed_house in item:

            # check of het geselecteerde huis niet zelfde is als huis waarmee je swapt
            if placed_house != selected_house and placed_house.size != selected_house.size:
                # sla de oude locaties van de huizen op in temporary variable
                temp_selected_bl = selected_house.bottom_left
                temp_placed_bl = placed_house.bottom_left

                # ruil de locaties om
                placed_house.location(temp_selected_bl)
                selected_house.location(temp_placed_bl)
                
                # bij algoritme 6 is het mogelijk huizen te draaien, waarbij de lengte en breedte draait
                if algoritme == 6:
                    swap = house.width
                    house.width = house.length
                    house.length = swap
                    house.location(house.bottom_left)

                # als beide huizen geplaatst kunnen worden op de nieuwe locaties
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

                    # als waarde niet hoger is
                    else:
                        # bij algoritme 6 is het mogelijk huizen te draaien, waarbij de lengte en breedte draait
                        if algoritme == 6:
                            house.length = house.width
                            house.width = swap
                            house.location(house.bottom_left)
                        # verander naar oude locatie en bereken opnieuw totale waarde
                        placed_house.location(temp_placed_bl)
                        selected_house.location(temp_selected_bl)
                        if place_house(selected_house, all_houses, waters) == True and place_house(placed_house, all_houses, waters) == True:
                            for item in all_houses.values():
                                for house in item:
                                    house.extra_meters()
                                    house.totalprice()

                # als huizen niet geplaatst kunnen worden 
                else:
                    # bij algoritme 6 is het mogelijk huizen te draaien, waarbij de lengte en breedte draait
                    if algoritme == 6:
                        house.length = house.width
                        house.width = swap
                        house.location(house.bottom_left)
                    # verplaats huizen naar oude locaties en bereken opnieuw totale waarde
                    placed_house.location(temp_placed_bl)
                    selected_house.location(temp_selected_bl)
                    if place_house(selected_house, all_houses, waters) == True and place_house(placed_house, all_houses, waters) == True:
                        for item in all_houses.values():
                            for house in item:
                                house.extra_meters()
                                house.totalprice()

    return all_houses, total_value_map_NEW