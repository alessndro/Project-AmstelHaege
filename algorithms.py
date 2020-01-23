from helpers_functions import *
def random_algoritme(number_of_houses, map_number):
    '''Random algorithm, all houses are assigned a spot on a random location '''

    # determine division houses
    number_small, number_medium, number_large = ratio_houses(number_of_houses)

    # create list of objects
    small_houses = create_house_object(number_small, "small")
    medium_houses = create_house_object(number_medium, "medium")
    large_houses = create_house_object(number_large, "large")
    waters = create_water_object(map_number)
    
    # save lists in dictionary
    all_houses = {}
    all_houses["small"] = small_houses
    all_houses["medium"] = medium_houses
    all_houses["large"] = large_houses

    # plaats alle huizen
    for house in all_houses["large"]:
        randomizer_algorithm(house, all_houses, waters)

    for house in all_houses["medium"]:
        randomizer_algorithm(house, all_houses, waters)

    for house in all_houses["small"]:
        randomizer_algorithm(house, all_houses, waters)

    total_value_map = 0
    for item in all_houses.values():
        for house in item:
            house.extra_meters()
            total_value_map += house.totalprice()

    return all_houses, total_value_map, waters

def randomizer_algorithm(house, all_houses, waters):
    '''Generates a random location and checks if the house can be placed on that location given the constraints '''

    while True:

        while True:
            # returns a tuple of a cordinate x,y bottom left of house
            bottom_left = randomizer()

            # check if bottom left, bottom right, top left and top right of house inside map
            if bottom_left[0] < MAXIMUM_WIDTH - house.width and bottom_left[1] < MAXIMUM_HEIGHT - house.length:
                house.location(bottom_left)
                break
        
        
        # Check of het huis geplaatst kan worden
        if place_house(house, all_houses, waters) == True:
            # als huis geplaatst mag worden, plaats huis
            house.placed = True
            break


def ascending_hillclimber(house, all_houses, waters, total_value_map):
    ''' Ascending hillclimber plaatst huizen op een nieuwe locatie afhankelijk van totale waarde kaart '''
    total_value_map_NEW = total_value_map

    # check in welke range het huis geplaats kan worden, niet kijkend naar water of andere 
    rangex = MAXIMUM_WIDTH - house.length
    rangey = MAXIMUM_HEIGHT - house.width
    # iterate over all cordinates
    for x in range(rangex):
        for y in range(rangey):
            if house.placed == True:
                tempx = house.bottom_left[0]
                tempy = house.bottom_left[1]
                # save cordinates house.bottom_left
                bottom_left = (x,y)
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

    
def greedy_algoritme(house, all_houses, waters):

    randomizer_algorithm(house, all_houses, waters)
    house.extra_meters()
    house.totalprice()

    total_value_map_NEW = 0
    # check in welke range het huis geplaats kan worden, niet kijkend naar water of andere 
    rangex = MAXIMUM_WIDTH - house.length
    rangey = MAXIMUM_HEIGHT - house.width
    # iterate over all cordinates
    for x in range(rangex):
        for y in range(rangey):
            tempx = house.bottom_left[0]
            tempy = house.bottom_left[1]
            # save cordinates house.bottom_left
            bottom_left = (x,y)
            # change cordinates of bl to new location
            house.location(bottom_left)
            # if you can place house on new location
            if place_house(house, all_houses, waters) == True:
                # bereken nieuw waarde map, waarin huis is verplaatst
                total_value_map_temp = 0
                for item in all_houses.values():
                    for selected_house in item:
                        if selected_house.placed == True:
                            selected_house.extra_meters()
                            total_value_map_temp += selected_house.totalprice()

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

def swap_houses(house, all_houses, waters, total_value_map):
    """swapt huizen en kijkt of de totale waarde verandert"""
    total_value_map_NEW = total_value_map
    selected_house = house

    for item in all_houses.values():
        for placed_house in item:
            if placed_house != selected_house:
                # sla de oude locaties van de huizen op
                temp_selected_bl = selected_house.bottom_left
                
                temp_placed_bl = placed_house.bottom_left

                placed_house.location(temp_selected_bl)

                selected_house.location(temp_placed_bl)
                
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
                    # als waarde niet hoger is verander naar oude locatie
                    else:
                        placed_house.location(temp_placed_bl)
                        selected_house.location(temp_selected_bl)
                        if place_house(selected_house, all_houses, waters) == True and place_house(placed_house, all_houses, waters) == True:
                            for item in all_houses.values():
                                for house in item:
                                    house.extra_meters()
                                    house.totalprice()
                    
                else:
                    placed_house.location(temp_placed_bl)
                    selected_house.location(temp_selected_bl)
                    if place_house(selected_house, all_houses, waters) == True and place_house(placed_house, all_houses, waters) == True:
                        for item in all_houses.values():
                            for house in item:
                                house.extra_meters()
                                house.totalprice()

    return all_houses, total_value_map_NEW