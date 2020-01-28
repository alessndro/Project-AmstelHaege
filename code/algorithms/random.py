#########################################################################
# random.py
#
# Minor Programming 
#
# Kiara Evers, Alessandro Degenkamp, Daniel Siha
#
# Bevat het random algoritme
##########################################################################
from .hf import *
from code.writer import *
import copy

def random_start(number_of_houses, map_number, turns):
    ''' zorgt ervoor dat het random algorite x aantal keer wordt uitgevoerd '''
    total_value_map = 0
    for i in range(turns):
        # voert het algoritme uit
        all_houses, total_value, waters = random_algoritme(number_of_houses, map_number)
        # schrijft de resultaten van deze run op om dit te kunnen plotten
        write_progress_run(number_of_houses=number_of_houses, map_number=map_number, total_value_map=total_value)
        # als de waarde hoger is dan de vorige waarde, sla deze op als nieuwe waarde
        if total_value > total_value_map:
            total_value_map = total_value
            all_houses_dic = copy.deepcopy(all_houses)
    
    return total_value, all_houses_dic, waters 

def random_algoritme(number_of_houses, map_number):
    ''' Random algoritme, alle huizen worden toegewezen aan een plek op een random locatie '''

    # bepaal verdeling van huizen
    number_small, number_medium, number_large = ratio_houses(number_of_houses)

    # maak lijst van de huis objecten
    small_houses = create_house_object(number_small, "small")
    medium_houses = create_house_object(number_medium, "medium")
    large_houses = create_house_object(number_large, "large")
    waters = create_water_object(map_number)
    
    # sla de lijsten op in een dictionary 
    all_houses = {}
    all_houses["small"] = small_houses
    all_houses["medium"] = medium_houses
    all_houses["large"] = large_houses

    # plaats alle huizen met het randomizer_algoritme
    for house in all_houses["large"]:
        randomizer_algorithm(house, all_houses, waters)

    for house in all_houses["medium"]:
        randomizer_algorithm(house, all_houses, waters)

    for house in all_houses["small"]:
        randomizer_algorithm(house, all_houses, waters)

    # initialiseer totale waarde map
    total_value_map = 0

    # itereer over alle huizen
    for item in all_houses.values():
        for house in item:
            # bereken prijs stijging door extra meters 
            house.extra_meters()
            # voegt totale prijs van elk huis steeds toe aan totale waarde map
            total_value_map += house.totalprice()

    return all_houses, total_value_map, waters

def randomizer_algorithm(house, all_houses, waters):
    ''' Genereert een random locatie en checkt of het huis geplaatst kan worden op die locatie kijkend naar de restricties '''

    # hoofdloop voor steeds opnieuw locatie zoeken
    while True:
        # loop kijkend of het gevonden punt binnen de map valt
        while True:
            # returns een tuple van x en y coördinaat van de linker onder hoek van het huis
            bottom_left = randomizer()

            # controleert of de linker onder hoek voldoende in map staat, zodat alle hoeken in de map vallen
            if bottom_left[0] < MAXIMUM_WIDTH - house.width and bottom_left[1] < MAXIMUM_HEIGHT - house.length:
                house.location(bottom_left)
                break
         
        # als huis geplaatst mag worden, plaats huis
        if place_house(house, all_houses, waters) == True:
            house.placed = True
            break