#########################################################################
# hf.py
#
# Minor programmeren
#
# Kiara Evers, Alessandro Degenkamp, Daniel Siha
#
# Bevat alle hulp functies die worden gebruikt bij de algoritmes
##########################################################################

from code.classes.models import House, Water
from random import seed, random
import math

# constanten
RATIO_SMALL = 0.6
RATIO_MEDIUM = 0.25
RATIO_LARGE = 0.15
MAXIMUM_HEIGHT = 180
MAXIMUM_WIDTH = 160
WIDTH_LENGTH_SMALL_HOUSE = 8

def place_house(selected_house, all_houses, waters):
    '''bepaald of een huis op de gekozen locate geplaatst kan worden en slaat de afstand tot het andere huis op in het object '''

    # controleert of de hoeken van het huis in water vallen
    for water in waters:
        if water.bottom_left[0] <= selected_house.bottom_left[0] <= water.bottom_right[0] and water.bottom_left[1] <= selected_house.bottom_left[1] <= water.top_left[1]:   
            return False
        if water.bottom_left[0] <= selected_house.bottom_right[0] <= water.bottom_right[0] and water.bottom_right[1] <= selected_house.bottom_right[1] <= water.top_right[1]:   
            return False
        if water.bottom_left[0] <= selected_house.top_left[0] <= water.bottom_right[0] and water.bottom_left[1] <= selected_house.top_left[1] <= water.top_left[1]:   
            return False
        if water.bottom_left[0] <= selected_house.top_right[0] <= water.bottom_right[0] and water.bottom_right[1] <= selected_house.top_right[1] <= water.top_right[1]:   
            return False

    # berekent de afstand tot de al geplaatste huizen
    for key in all_houses.values():
        for placed_house in key:
            # controleer of het huis geplaatst is, en of je niet vergelijkt met hetzelfde huis
            if (placed_house.placed == True) and (selected_house != placed_house):
                # berekent de afstand van het te plaatsen huis tot het geplaatste huis
                distance = distance_berekening(selected_house, placed_house)
                
                # controleert of de afstand voldoet aan de verplichte vrijstand van het te plaatsen huis en het geplaatste huis
                if distance <= placed_house.obligated_space or distance <= selected_house.obligated_space:
                    return False
                
                # slaat de afstand op in beide objecten
                selected_house.compared_space(placed_house, distance)
                placed_house.compared_space(selected_house, distance)

    return True

def distance_berekening(selected_house, placed_house):
    ''' berekent de afstand van het geselecteerde huis tot het al geplaatste huis'''

    # geplaatste huis zit links t.o.v. de x-as van het geselecteerde huis
    if placed_house.bottom_right[0] <= selected_house.top_left[0]: 
        # linksboven
        if placed_house.bottom_right[1] >= selected_house.top_left[1]:
            delta_x_sq = (selected_house.top_left[0]-placed_house.bottom_right[0])**(2)
            delta_y_sq = (placed_house.bottom_right[1]-selected_house.top_left[1])**(2)
            distance = math.sqrt(delta_x_sq + delta_y_sq)
        # links onder
        elif placed_house.top_right[1] <= selected_house.bottom_left[1]:
            delta_x_sq = (selected_house.top_left[0]-placed_house.bottom_right[0])**(2)
            delta_y_sq = (selected_house.bottom_left[1] - placed_house.top_right[1])**(2)
            distance = math.sqrt(delta_x_sq + delta_y_sq)
        # linksmidden
        else:
            distance = selected_house.bottom_left[0] - placed_house.bottom_right[0]
            

    # geplaatste huis zit rechts t.o.v. de x-as van het geselecteerde huis
    elif placed_house.bottom_left[0] >= selected_house.top_right[0]:
        # rechtsboven
        if placed_house.bottom_left[1] >= selected_house.top_right[1]:
            delta_x_sq = (placed_house.bottom_left[0]-selected_house.top_right[0])**(2)
            delta_y_sq = (placed_house.bottom_left[1]-selected_house.top_right[1])**(2)
            distance = math.sqrt(delta_x_sq + delta_y_sq)

        # rechtsonder
        elif placed_house.top_left[1] <= selected_house.bottom_right[1]:
            delta_x_sq = (placed_house.top_left[0]-selected_house.bottom_right[0])**(2)
            delta_y_sq = (selected_house.bottom_right[1]-placed_house.top_left[1])**(2)
            distance = math.sqrt(delta_x_sq + delta_y_sq)
        # rechtsmidden
        else:
            distance = placed_house.top_left[0] - selected_house.top_right[0]
            
    # geplaatste huis zit niet volledig links en niet rechts t.o.v. de x-as van het geselecteerde huis
    else:
        # boven
        if placed_house.bottom_left[1] >= selected_house.top_left[1]:
            distance = placed_house.bottom_left[1] - selected_house.top_left[1]
        # onder
        else:
            distance = selected_house.bottom_left[1] - placed_house.top_left[1]

    return distance

def randomizer():
    ''' Generates a random x and y value'''
    random_x = math.floor(random()*MAXIMUM_HEIGHT)
    random_y = math.floor(random()*MAXIMUM_WIDTH)

    return (random_x, random_y)

def ratio_houses(number_of_houses):
    '''Verdeelt het aantal huizen op basis van het aantal gekozen huizen naar verhouding van de gegeven ratio'''
    small = int(RATIO_SMALL * number_of_houses)
    medium = int(RATIO_MEDIUM * number_of_houses)
    large = int(RATIO_LARGE * number_of_houses)
    
    return (small, medium, large)


def create_house_object(house_size, house_sort):
    '''Maakt alle huis objecten aan voor het gegeven huis soort en vult deze met de basis informatie'''
    list_of_objects = []
    count = 0
    # voegt alle gegeven waardes toe aan de objecten en maakt de objecten aan met unieke eigen naam
    if house_sort == "small":
        for i in range(house_size):
            name = "S" + str(count)
            small = House(name=name, size=house_sort, start_value=285000, obligated_space=2, rate=0.03, length=8, width=8)
            list_of_objects.append(small)
            count += 1
    if house_sort == "medium":
        for i in range(house_size):
            name = "M" + str(count)
            medium = House(name=name, size=house_sort, start_value=399000, obligated_space=3, rate=0.04, length=7, width=11)
            list_of_objects.append(medium)
            count += 1
    if house_sort == "large":
        for i in range(house_size):
            name = "L" + str(count)
            large = House(name=name, size=house_sort, start_value=610000, obligated_space=6, rate=0.06, length=10, width=12)
            list_of_objects.append(large)
            count += 1

    return list_of_objects

def create_water_object(map_number):
    '''Creert de water objecten aan de hand van de gekozen kaart'''
    waters = []
    if map_number == 1:
        water = Water(map=1, top_right=(32,180), top_left=(0,180), bottom_right=(32,0), bottom_left=(0,0))
        waters.append(water)
    elif map_number == 2:
        water = Water(map=2, top_right=(32,55), top_left=(0,55), bottom_right=(32,0), bottom_left=(0,0))
        waters.append(water)
        water = Water(map=2, top_right=(160,32), top_left=(135,32), bottom_right=(160,0), bottom_left=(135,0))
        waters.append(water)
        water = Water(map=2, top_right=(45,180), top_left=(0,180), bottom_right=(45,128), bottom_left=(0,128))
        waters.append(water)
        water = Water(map=2, top_right=(160,180), top_left=(135,180), bottom_right=(160,128), bottom_left=(135,128))
        waters.append(water)
    elif map_number == 3:
        water0 = Water(map=3, top_right=(116,130), top_left=(44,130), bottom_right=(116,50), bottom_left=(44,50))
        waters.append(water0)

    return waters

def get_input():
    '''Vraagt de gebruiker om de benodigde informatie om het algoritme uit te kunnen voeren'''

    # vraagt om input van gebruiker, over welke kaart, hoeveel huizen en welk algoritme zij willen uitvoeren
    while True:
        number_of_houses = int(input("Wat is het aantal huizen, 20, 40 of 60?: \n"))

        map_number = int(input("Welke map wilt u gebruiken? 1,2,3: \n"))

        algoritme = int(input("Welk algoritme wilt u gebruiken? \n" +
        "1 for random algorithm \n"  + 
        "2 voor ascending hillclimber \n" +
        "3 voor greedy \n" +
        "4 voor swappinghouses \n" +
        "5 voor random points ascending hillclimber \n" +
        "6 voor combinatie van greedy en swappinghouses waarbij ze ook 90 graden gedraaid kunnen worden \n" ))
        
        # als de juiste waarden worden gekozen, begin het programma
        if (number_of_houses == 20 or number_of_houses == 40 or number_of_houses == 60) and (map_number > 0 and map_number <= 3) and algoritme > 0 and algoritme < 7:
            break
        
    return number_of_houses, map_number, algoritme

