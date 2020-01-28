#########################################################################
# greedy.py
#
# Minor Programming 
#
# Kiara Evers, Alessandro Degenkamp, Daniel Siha
#
# Bevat het greedy algoritme
##########################################################################
from .hf import *
from .random import randomizer_algorithm

def greedy(number_of_houses, map_number, waters, total_value_map):
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

    # loop door alle huizen en plaats deze op de meest gunstige plek zodat de waarde van de kaart het hoogst is
    for house in all_houses_dic["large"]:
        all_houses_dic, total_value = greedy_algoritme(house, all_houses_dic, waters)

    for house in all_houses_dic["medium"]:
        all_houses_dic, total_value = greedy_algoritme(house, all_houses_dic, waters)

    for house in all_houses_dic["small"]:
            all_houses_dic, total_value = greedy_algoritme(house, all_houses_dic, waters)

    
    return total_value, all_houses_dic, waters

def greedy_algoritme(house, all_houses, waters):
    ''' Greedy algoritme plaats huis eerst op random locatie, zoekt vervolgens andere locatie met hogere totale waarde map '''
    
    # per huis plaats op random locatie en bereken totale waarde map
    randomizer_algorithm(house, all_houses, waters)
    house.extra_meters()
    house.totalprice()

    # initialiseer nieuwe totale waarde map
    total_value_map_NEW = 0

    # check in welke range het huis geplaats kan worden, niet kijkend naar water of andere huizen
    rangex = MAXIMUM_WIDTH - house.length
    rangey = MAXIMUM_HEIGHT - house.width

    # itereer over alle coördinaten van de map
    for x in range(rangex):
        for y in range(rangey):

            # sla oude coördinaat op
            tempx = house.bottom_left[0]
            tempy = house.bottom_left[1]
            
            # verander locatie van huis naar nieuwe locatie
            bottom_left = (x,y)
            house.location(bottom_left)

            # bereken nieuw waarde map, waarin huis is verplaatst
            if place_house(house, all_houses, waters) == True:
                total_value_map_temp = 0
                for item in all_houses.values():
                    for selected_house in item:
                        if selected_house.placed == True:
                            selected_house.extra_meters()
                            total_value_map_temp += selected_house.totalprice()

                # als waarde met nieuwe locatie hoger is, verander deze
                if total_value_map_NEW < total_value_map_temp:
                    total_value_map_NEW = total_value_map_temp
                    
                # als waarde niet hoger is verander naar oude locatie en bereken weer totale waarde map
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