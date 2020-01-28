#########################################################################
# random_points_ascending_hillclimber.py
#
# Minor Programming 
#
# Kiara Evers, Alessandro Degenkamp, Daniel Siha
#
# Bevat het random ascending hill climber algoritme
##########################################################################
from .hf import *
from .random import random_algoritme
import copy

def random_ascending_hillclimber_algoritme(number_of_houses, map_number):
    ''' plaatst alle huizen op een random locatie, en zoekt dan per huis een aantal random locaties en kijkt of hiermee de waarde van de map te verhogen is '''

    # plaatst alle huizen op een random locatie
    all_houses, total_value, waters = random_algoritme(number_of_houses, map_number)

    # roept random hillclimber aan, deze pakt een bestaand huis, en kijkt voor een aantal punten wat de beste plek zou zijn om dit huis te plaatsen
    for item in all_houses.values():
        for house in item:
            all_houses_new, total_value = random_ascending_hillclimber(house=house, all_houses=all_houses, waters=waters, total_value_map=total_value)
    all_houses_dic = copy.deepcopy(all_houses_new)
    
    return total_value, all_houses_dic, waters

def random_points_ascending_hillclimber(house, all_houses, waters, total_value_map):
    ''' Pakt random een gekozen aantal punten per huis en kijkt of op die locaties totale waarde van de map hoger wordt '''
   
    # initialiseer nieuwe totale waarde map
    total_value_map_NEW = total_value_map

    # check in welke range het huis geplaats kan worden, niet kijkend naar water of andere huizen
    rangex = MAXIMUM_WIDTH - house.width
    rangey = MAXIMUM_HEIGHT - house.length

    # range die aangeeft hoeveel random punten algoritme langs gaat
    for x in range(1000):

        # maak random x en y coördinaat
        randomizex = 0 + rangex * random()
        randomizey = 0 + rangey * random()

        # sla oude coördinaat op
        tempx = house.bottom_left[0]
        tempy = house.bottom_left[1]

        # verander locatie van huis naar nieuwe locatie
        bottom_left = (randomizex,randomizey)
        house.location(bottom_left)

        # als het huis op de nieuwe locatie geplaatst kan worden
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

            # als waarde niet hoger is, verander naar oude locatie en bereken weer totale waarde map
            else:
                bottom_left = (tempx,tempy)
                house.location(bottom_left)
                if place_house(house, all_houses, waters) == True:
                    for item in all_houses.values():
                        for houses in item:
                            houses.extra_meters()
                            houses.totalprice()

        # als huis niet geplaats kan worden, verander naar oude locatie en bereken weer totale waarde map
        else:
            bottom_left = (tempx,tempy)
            house.location(bottom_left)
            if place_house(house, all_houses, waters) == True:
                    for item in all_houses.values():
                        for houses in item:
                            houses.extra_meters()
                            houses.totalprice()

    return all_houses, total_value_map_NEW