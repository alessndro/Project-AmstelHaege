#########################################################################
# algorithms.py
#
# Minor Programming 
#
# Kiara Evers, Alessandro Degenkamp, Daniel Siha
#
# Bevat alle algoritmes de worden gebruikt in dit project
##########################################################################

from hf import *

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

def random_ascending_hillclimber(house, all_houses, waters, total_value_map):
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

random_algoritme(1,1)

def ratio_houses(number_of_houses):
    '''Verdeelt het aantal huizen op basis van het aantal gekozen huizen naar verhouding van de gegeven ratio'''
    small = int(RATIO_SMALL * number_of_houses)
    medium = int(RATIO_MEDIUM * number_of_houses)
    large = int(RATIO_LARGE * number_of_houses)
    
    return (small, medium, large)