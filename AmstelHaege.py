from models import House, Water
from random import seed
from random import random
import _random
import math
import csv
#from coede.visualitastion import visualise as vis

# Import the necessary packages and modules for matplotlib
import matplotlib.pyplot as plt
import numpy as np

#constants
ratio_small = 0.6
ratio_medium = 0.25
ratio_large = 0.15
maximum_height = 180
maximum_width = 160
width_length_small_house = 8

def main():
    
    seed(3)
    # ask user for number of houses to be placed
    while True:
        number_of_houses = int(input("What are the amount of Houses 20, 40 or 60?"))

        if number_of_houses == 20 or number_of_houses == 40 or number_of_houses == 60:
            break

    # determine division houses
    number_small, number_medium, number_large = ratio_houses(number_of_houses)

    # create list of objects
    small_houses = create_house_object(number_small, "small")
    medium_houses = create_house_object(number_medium, "medium")
    large_houses = create_house_object(number_large, "large")
    
    # save lists in dictionary
    all_houses = {}
    all_houses["small"] = small_houses
    all_houses["medium"] = medium_houses
    all_houses["large"] = large_houses

    # plaats alle huizen
    for item in all_houses.values():
        for house in item:
            algoritme(house, all_houses)
            print("NAAM EN GEPLAATS PLUS CORDINAAT", house.name, house.placed, house.bottom_left)
        
    # bereken alle afstanden tot alle huizen
    for item in all_houses.values():
        for house in item:
            bereken(house, all_houses)

    total_value_map = 0
    for item in all_houses.values():
        for house in item:
            house.extra_meters()
            total_value_map += house.totalprice()

    print(total_value_map)
        



def algoritme(house, all_houses):

    while True:

        # returns a tuple of a cordinate x,y bottom left of house
        bottom_left = randomizer()
        house.location(bottom_left)

        # Check of het huis geplaatst kan worden
        if place_house(house, all_houses) == True:
            # als huis geplaatst mag worden, plaats huis
            house.placed = True
            break


def place_house(selected_house, all_houses):
    '''Bepaald of een huis op de gekozen locatie geplaatst kan worden '''
    house = selected_house
    # check if bottom left, bottom right, top left and top right of house overlap water
    # if water.bottom_left[0] <= house.bottom_left[0] <= water.bottom_right[0] and water.top_left[1] <= house.bottom_left[1] <= water.bottom_left[1]:   
    #     return False
        
    # if water.bottom_left[0] <= house.bottom_right[0] <= water.bottom_right[0] and water.top_left[1] <= house.bottom_right[1] <= water.bottom_left[1]:   
    #     return False

    # if water.bottom_left[0] <= house.top_left[0] <= water.bottom_right[0] and water.top_left[1] <= house.top_left[1] <= water.bottom_left[1]:   
    #     return False

    # if water.bottom_left[0] <= house.top_right[0] <= water.bottom_right[0] and water.top_left[1] <= house.top_right[1] <= water.bottom_left[1]:   
    #     return False

    for item in all_houses.values():
        for current_house_to_check in item:
             # check if given cordinates of new house overlaps with houses and obligated space
            if current_house_to_check.placed == True and selected_house != current_house_to_check:
                houseplaced = current_house_to_check
        
                # add obligated space with surface of house dependant on size
                if houseplaced.size == "small":
                    # calculate bottom left of house and obligatory space/garden
                    houseandgarden_bottom_left = ((houseplaced.bottom_left[0] - 2),(houseplaced.bottom_left[1] - 2))

                    # calculate bottom right of house and obligatory space/garden
                    houseandgarden_bottom_right = ((houseplaced.bottom_right[0] + 2),(houseplaced.bottom_right[1] - 2))

                    # calculate top left of house and obligatory space/garden
                    houseandgarden_top_left = ((houseplaced.top_left[0] - 2),(houseplaced.top_left[1] + 2))
                    
                    # check whether both x and y cordinates of all four corners of new house not inside already placed house and garden
                    if houseandgarden_bottom_left[0] <= house.bottom_left[0] <= houseandgarden_bottom_right[0] and houseandgarden_top_left[1] <= house.bottom_left[1] <= houseandgarden_bottom_left[1]:
                        return False
                    if houseandgarden_bottom_left[0]  <= house.bottom_right[0] <= houseandgarden_bottom_right[0] and houseandgarden_top_left[1] <= house.bottom_right[1] <= houseandgarden_bottom_left[1]:   
                        return False
                    if houseandgarden_bottom_left[0]  <= house.top_left[0] <= houseandgarden_bottom_right[0] and houseandgarden_top_left[1] <= house.top_left[1] <= houseandgarden_bottom_left[1]:   
                        return False
                    if houseandgarden_bottom_left[0]  <= house.top_right[0] <= houseandgarden_bottom_right[0] and houseandgarden_top_left[1] <= house.top_right[1] <= houseandgarden_bottom_left[1]:   
                        return False
                
                if houseplaced.size == "medium":
                    # calculate bottom left of house and obligatory space/garden
                    houseandgarden_bottom_left = ((houseplaced.bottom_left[0] - 3),(houseplaced.bottom_left[1] - 3))
                    # calculate bottom right of house and obligatory space/garden
                    houseandgarden_bottom_right = ((houseplaced.bottom_right[0] + 3),(houseplaced.bottom_right[1] - 3))
                    # calculate top left of house and obligatory space/garden
                    houseandgarden_top_left = ((houseplaced.top_left[0] - 3),(houseplaced.top_left[1] + 3))

                    # check whether both x and y cordinates of all four corners of new house not inside already placed house and garden
                    if houseandgarden_bottom_left[0] <= house.bottom_left[0] <= houseandgarden_bottom_right[0] and houseandgarden_top_left[1] <= house.bottom_left[1] <= houseandgarden_bottom_left[1]:
                        return False

                    if houseandgarden_bottom_left[0]  <= house.bottom_right[0] <= houseandgarden_bottom_right[0] and houseandgarden_top_left[1] <= house.bottom_right[1] <= houseandgarden_bottom_left[1]:   
                        return False

                    if houseandgarden_bottom_left[0]  <= house.top_left[0] <= houseandgarden_bottom_right[0] and houseandgarden.top_left[1] <= house.top_left[1] <= houseandgarden_bottom_left[1]:   
                        return False

                    if houseandgarden_bottom_left[0]  <= house.top_right[0] <= houseandgarden_bottom_right[0] and houseandgarden.top_left[1] <= house.top_right[1] <= houseandgarden_bottom_left[1]:   
                        return False

                if houseplaced.size == "large":
                    # bottom left of house and obligatory space/garden
                    houseandgarden_bottom_left = ((houseplaced.bottom_left[0] - 6),(houseplaced.bottom_left[1] - 6))
                    # bottom right of house and obligatory space/garden
                    houseandgarden_bottom_right = ((houseplaced.bottom_right[0] + 6),(houseplaced.bottom_right[1] - 6))
                    # top left of house and obligatory space/garden
                    houseandgarden_top_left = ((houseplaced.top_left[0] - 6),(houseplaced.top_left[1] + 6))
                
                    # check whether both x and y cordinates of all four corners of new house not inside already placed house and garden
                    if houseandgarden_bottom_left[0] <= house.bottom_left[0] <= houseandgarden_bottom_right[0] and houseandgarden_top_left[1] <= house.bottom_left[1] <= houseandgarden_bottom_left[1]:
                        return False

                    if houseandgarden_bottom_left[0]  <= house.bottom_right[0] <= houseandgarden_bottom_right[0] and houseandgarden_top_left[1] <= house.bottom_right[1] <= houseandgarden_bottom_left[1]:   
                        return False

                    if houseandgarden_bottom_left[0]  <= house.top_left[0] <= houseandgarden_bottom_right[0] and houseandgarden_top_left[1] <= house.top_left[1] <= houseandgarden_bottom_left[1]:   
                        return False

                    if houseandgarden_bottom_left[0]  <= house.top_right[0] <= houseandgarden_bottom_right[0] and houseandgarden_top_left[1] <= house.top_right[1] <= houseandgarden_bottom_left[1]:   
                        return False

            return True

def randomizer():
    ''' Generates a random x and y value'''
    # Daniel wil seed later gebruiken, zorgt voor zelfde uitkomst okal random
    # Kiara eandgarden_wil math.floor verwijderen voor exacte cordinaten ipv grid
    random_x = math.floor(random()*maximum_height)
    random_y = math.floor(random()*maximum_width)
    return (random_x, random_y)

def ratio_houses(number_of_houses):
    '''Determines number of houses per size house '''
    small = int(ratio_small * number_of_houses)
    medium = int(ratio_medium * number_of_houses)
    large = int(ratio_large * number_of_houses)
    
    return (small, medium, large)

def create_house_object(house_size, house_sort):
    '''Creates all the objects for a particular house and returns a list'''
    list_of_objects = []

    if house_sort == "small":
        count = 0
        for i in range(house_size):
            name = "S" + str(count)
            small = House(name=name, size=house_sort, start_value=285.000, obligated_space=2, rate=0.03, length=8, width=8)
            list_of_objects.append(small)
            count += 1
    if house_sort == "medium":
        count = 0
        for i in range(house_size):
            name = "M" + str(count)
            medium = House(name=name, size=house_sort, start_value=399.000, obligated_space=3, rate=0.04, length=11, width=7)
            list_of_objects.append(medium)
            count += 1
    if house_sort == "large":
        count = 0
        for i in range(house_size):
            name = "L" + str(count)
            large = House(name=name, size=house_sort, start_value=610.000, obligated_space=6, rate=0.06, length=12, width=10)
            list_of_objects.append(large)
            count += 1
    return list_of_objects

# # vul object huis in met bottom_left coordinaten
# def fill_information_house(bottom_left, house):
#     '''Vult alle coordinaten in van het object op basis van het random punt dat is gekozen ''' 
#     if house_size == small:
#         count = 0
#         for i in range(8):
#             for j in range(8):
#                 bottom_left(: + i ,: + j) = "s" + count
#                 count += 1

def bereken(selected_house, placed_houses):

    for item in placed_houses.values():
        for placed_house in item:
        
            if selected_house != placed_house:
                # onder
                if placed_house.bottom_left[1] <= selected_house.bottom_left[1] and (selected_house.top_left[0] <= placed_house.bottom_left[0] <= selected_house.top_right[0] or selected_house.top_left[0] <= placed_house.bottom_right[0] <= selected_house.top_right[0]):
                    distance = selected_house.bottom_left[1] - placed_house.top_left[1]
                    print("onder")
                # boven
                if placed_house.bottom_right[1] >=  selected_house.top_right[1] and (selected_house.bottom_left[0] <= placed_house.bottom_right[0] <= selected_house.top_left[0] or selected_house.bottom_left[0] <= placed_house.bottom_left[0] <= selected_house.top_left[0]):
                    distance = placed_house.bottom_right[1]-selected_house.top_right[1]
                    print("boven")
                #links
                if placed_house.bottom_right[0] <= selected_house.bottom_right[0] and (selected_house.bottom_left[1] <= placed_house.bottom_right[1] <= selected_house.top_left[1] or selected_house.bottom_left[1] <= placed_house.top_right[1] <= selected_house.top_left[1]):
                    distance = selected_house.bottom_left[0]-placed_house.bottom_right[0]
                    print("links")
                #rechts
                if placed_house.bottom_right[0] >= selected_house.bottom_left[0] and (selected_house.bottom_left[1] <= placed_house.bottom_right[1] <= selected_house.top_left[1] or selected_house.bottom_left[1] <= placed_house.top_right[1] <= selected_house.top_left[1]):
                    distance = placed_house.bottom_right[0] - selected_house.bottom_left[0]
                    print("rechts")
                # linksboven 
                if selected_house.top_left[0] > placed_house.bottom_right[0] and selected_house.top_left[1] < placed_house.bottom_right[1]:
                    distance = math.sqrt((selected_house.top_left[0]-placed_house.bottom_right[0])**(2))+((placed_house.bottom_right[1]-selected_house.top_left[1])**(2))
                    print("linksboven")
                # rechtsboven
                if selected_house.top_right[0] < placed_house.bottom_left[0] and selected_house.top_right[1] < placed_house.bottom_left[1]:
                    distance = math.sqrt((placed_house.bottom_left[0]-selected_house.top_right[0])**(2))+((placed_house.bottom_left[1]-placed_house.top_right[1])**(2))
                    print("rechtsboven")
                # rechtsonder
                if selected_house.bottom_right[0] < placed_house.top_left[0] and selected_house.bottom_right[1] > placed_house.top_left[1]:
                    distance = math.sqrt((placed_house.top_left[0]-selected_house.top_right[0])**(2))+((selected_house.bottom_right[1]-selected_house.top_left[1])**(2))
                    print("rechtsonder")
                # linksonder
                if selected_house.bottom_left[0] > placed_house.top_right[0] and selected_house.bottom_left[1] > placed_house.top_right[1]:
                    distance = math.sqrt((selected_house.bottom_left[0]-placed_house.top_right[0])**(2))+((selected_house.bottom_left[1]-placed_house.top_right[1])**(2))
                    print("linksonder")
                print(distance)
                selected_house.compared_space(placed_house, distance)

                # COORDINATEN WONINGEN NIET BUITEN DE KAART
                # EXTRA CONTROLE TOEVOEGEN



if __name__ == "__main__":
    main()