#########################################################################
# ascending_hillclimber.py
#
# Minor Programming 
#
# Kiara Evers, Alessandro Degenkamp, Daniel Siha
#
# Bevat het ascending hillclimber algoritme
##########################################################################
from .random import *

def asceding_hillclimber_algoritme(number_of_houses, map_number, all_houses, waters, total_value_map):
    ''' zorgt ervoor dat er een ascending hillclimber wordt uitgevoerd '''
    # plaatst alle huizen random op de kaart
    all_houses, total_value, waters = random_algoritme(number_of_houses, map_number)
    
    # verplaatst alle huizen, probeert elke mogelijke plek uit en bewaard de beste positie waarmee de waarde van de kaart hoger is
    for item in all_houses.values():
        for house in item:
            all_houses_dic, total_value = ascending_hillclimber(house=house, all_houses=all_houses, waters=waters, total_value_map=total_value_map)  

    return total_value, all_houses_dic, waters

def ascending_hillclimber(house, all_houses, waters, total_value_map):
    ''' Ascending hillclimber plaatst huizen op een nieuwe locatie afhankelijk van totale waarde kaart '''
    
    # initialiseer totale map waarde
    total_value_map_NEW = total_value_map

    # check in welke range het huis geplaats kan worden, niet kijkend naar water of andere huizen
    rangex = MAXIMUM_WIDTH - house.length
    rangey = MAXIMUM_HEIGHT - house.width

    # itereer over alle coördinaten van de map
    for x in range(rangex):
        for y in range(rangey):

            # als het huis geplaatst kan worden
            if house.placed == True:

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
                        for house in item:
                            house.extra_meters()
                            total_value_map_temp += house.totalprice()

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