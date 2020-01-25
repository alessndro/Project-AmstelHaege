from models import House, Water
from random import seed, random
import math

#constants
RATIO_SMALL = 0.6
RATIO_MEDIUM = 0.25
RATIO_LARGE = 0.15
MAXIMUM_HEIGHT = 180
MAXIMUM_WIDTH = 160
WIDTH_LENGTH_SMALL_HOUSE = 8

def place_house(selected_house, all_houses, waters):
    '''Bepaald of een huis op de gekozen locate geplaatst kan worden '''

    for water in waters:
        distance = distance_berekening(selected_house, water)
        if distance <= 0:
            return False

        if water.bottom_left[0] <= selected_house.bottom_left[0] <= water.bottom_right[0] and water.bottom_left[1] <= selected_house.bottom_left[1] <= water.top_left[1]:   
            return False
        if water.bottom_left[0] <= selected_house.bottom_right[0] <= water.bottom_right[0] and water.bottom_right[1] <= selected_house.bottom_right[1] <= water.top_right[1]:   
            return False
        if water.bottom_left[0] <= selected_house.top_left[0] <= water.bottom_right[0] and water.bottom_left[1] <= selected_house.top_left[1] <= water.top_left[1]:   
            return False
        if water.bottom_left[0] <= selected_house.top_right[0] <= water.bottom_right[0] and water.bottom_right[1] <= selected_house.top_right[1] <= water.top_right[1]:   
            return False

    

    for key in all_houses.values():
        for placed_house in key:
            if (placed_house.placed == True) and (selected_house != placed_house):
                distance = distance_berekening(selected_house, placed_house)
                # HIER DE = NOG WEGHALEN LATER
                if distance <= placed_house.obligated_space or distance <= selected_house.obligated_space:
                    return False
                selected_house.compared_space(placed_house, distance)
                placed_house.compared_space(selected_house, distance)
    return True


def distance_berekening(selected_house, placed_house):

    # links op de x-as
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
            

    # rechts op de x-as
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
            
    # BOVEN OF ONDER
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
    # Daniel wil seed later gebruiken, zorgt voor zelfde uitkomst okal random
    # Kiara eandgarden_wil math.floor verwijderen voor exacte cordinaten ipv grid
    random_x = math.floor(random()*MAXIMUM_HEIGHT)
    random_y = math.floor(random()*MAXIMUM_WIDTH)
    return (random_x, random_y)

def ratio_houses(number_of_houses):
    '''Determines number of houses per size house '''
    small = int(RATIO_SMALL * number_of_houses)
    medium = int(RATIO_MEDIUM * number_of_houses)
    large = int(RATIO_LARGE * number_of_houses)
    
    return (small, medium, large)

def create_house_object(house_size, house_sort):
    '''Creates all the objects for a particular house and returns a list'''
    list_of_objects = []

    if house_sort == "small":
        count = 0
        for i in range(house_size):
            name = "S" + str(count)
            small = House(name=name, size=house_sort, start_value=285000, obligated_space=2, rate=0.03, length=8, width=8)
            list_of_objects.append(small)
            count += 1
    if house_sort == "medium":
        count = 0
        for i in range(house_size):
            name = "M" + str(count)
            medium = House(name=name, size=house_sort, start_value=399000, obligated_space=3, rate=0.04, length=7, width=11)
            list_of_objects.append(medium)
            count += 1
    if house_sort == "large":
        count = 0
        for i in range(house_size):
            name = "L" + str(count)
            large = House(name=name, size=house_sort, start_value=610000, obligated_space=6, rate=0.06, length=10, width=12)
            list_of_objects.append(large)
            count += 1
    return list_of_objects

def create_water_object(map_number):
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

    # vraagt om input van gebruiker, over welke kaart, hoeveel huizen en welk algoritme zij willen uitvoeren
    while True:
        number_of_houses = int(input("What are the amount of Houses 20, 40 or 60?"))

        map_number = int(input("Which map would you like to use? 1,2,3"))

        algoritme = int(input("Which algorithm would you like to use?  press 1 for random algorithm, 2 for ascending hillclimber, 3 for greedy, 4 for swappinghouses, 5 for double random"))
        
        # als de juiste waarden worden gekozen, begin het programma
        if (number_of_houses == 20 or number_of_houses == 40 or number_of_houses == 60) and (map_number > 0 and map_number <= 3) and algoritme > 0 and algoritme < 7:
            break
        
    return number_of_houses, map_number, algoritme

def random(number_of_houses, map_number, total_value_map):
     if algoritme == 1:
        for i in range(1):
            all_houses, total_value, waters = random_algoritme(number_of_houses, map_number)
            write_progress(number_of_houses=number_of_houses, map_number=map_number, solution=count, total_value_map=total_value)
            write_progress_run(number_of_houses=number_of_houses, map_number=map_number, solution=count, total_value_map=total_value)
            if total_value > total_value_map:
                total_value_map = total_value
                all_houses_dic = copy.deepcopy(all_houses) #!!! dit was eerst een andere variabel
            count += 1

    
    return total_value, all_houses_dic, waters
        

def asceding_hillclimber_algoritme(number_of_houses, map_number, all_houses, waters, total_value_map):
    if algoritme == 2:
        all_houses, total_value, waters = random_algoritme(number_of_houses, map_number)
        for item in all_houses.values():
            for house in item:
                all_houses_dic, total_value = ascending_hillclimber(house=house, all_houses=all_houses, waters=waters, total_value_map=total_value_map)  
    
    return total_value, all_houses_dic, waters

def greedy(number_of_houses, map_number, all_houses, waters, total_value_map):
        # bepaal de verdeling van de huizen
        number_small, number_medium, number_large = ratio_houses(number_of_houses)

        # creeert lijsten met objecten van de juiste grootte
        small_houses = create_house_object(number_small, "small")
        medium_houses = create_house_object(number_medium, "medium")
        large_houses = create_house_object(number_large, "large")
        waters = create_water_object(map_number)

        # slaat de lijsten op in de dictionairy
        all_houses_dic["small"] = small_houses
        all_houses_dic["medium"] = medium_houses
        all_houses_dic["large"] = large_houses

        # loop door alle huizen en plaats deze op de meest gunstige plek
        for house in all_houses_dic["large"]:
            all_houses_dic, total_value = greedy_algoritme(house, all_houses_dic, waters)

        for house in all_houses_dic["medium"]:
            all_houses_dic, total_value = greedy_algoritme(house, all_houses_dic, waters)

        for house in all_houses_dic["small"]:
            all_houses_dic, total_value = greedy_algoritme(house, all_houses_dic, waters)

    
    return total_value, all_houses_dic, waters

def swapping_houses_algoritme(number_of_houses, map_number, all_houses, waters, total_value_map)):

        for i in range(1):
            all_houses, total_value, waters = random_algoritme(number_of_houses, map_number)
            write_progress(number_of_houses=number_of_houses, map_number=map_number, solution=count, total_value_map=total_value)
            write_progress_run(number_of_houses=number_of_houses, map_number=map_number, solution=count, total_value_map=total_value)
            count += 1
            if total_value > total_value_map:
                total_value_map = total_value
                print(total_value)
        for item in all_houses.values():
            for house in item:
                all_houses_new, total_value = swap_houses(house=house, all_houses=all_houses, waters=waters, total_value_map=total_value_map)
            
            all_houses_dic = copy.deepcopy(all_houses_new)
    
    return total_value, all_houses_dic, waters

def random_ascending_hillclimber_algoritme(number_of_houses, map_number, all_houses, waters, total_value_map)):

        for i in range(1):
            all_houses, total_value, waters = random_algoritme(number_of_houses, map_number)
            print("Total value Random", total_value)
            visualisation(all_houses=all_houses, waters=waters) 
            visualisation_plot()

        for item in all_houses.values():
            for house in item:
                all_houses_new, total_value = random_ascending_hillclimber(house=house, all_houses=all_houses, waters=waters, total_value_map=total_value)
        all_houses_dic = copy.deepcopy(all_houses_new)
    
    return total_value, all_houses_dic, waters

def swap_houses_after_greedy_algoritme(number_of_houses, map_number, all_houses, waters, total_value_map, algoritme)):
        # bepaal de verdeling van de huizen
        number_small, number_medium, number_large = ratio_houses(number_of_houses)

        # creeert lijsten met objecten van de juiste grootte
        small_houses = create_house_object(number_small, "small")
        medium_houses = create_house_object(number_medium, "medium")
        large_houses = create_house_object(number_large, "large")
        waters = create_water_object(map_number)

        # slaat de lijsten op in de dictionairy
        all_houses_dic["small"] = small_houses
        all_houses_dic["medium"] = medium_houses
        all_houses_dic["large"] = large_houses

        # loop door alle huizen en plaats deze op de meest gunstige plek
        for house in all_houses_dic["large"]:
            all_houses_dic, total_value = greedy_algoritme(house, all_houses_dic, waters)

        for house in all_houses_dic["medium"]:
            all_houses_dic, total_value = greedy_algoritme(house, all_houses_dic, waters)

        for house in all_houses_dic["small"]:
            all_houses_dic, total_value = greedy_algoritme(house, all_houses_dic, waters)

        visualisation(all_houses=all_houses_dic, waters=waters) 
        visualisation_plot()
        print(total_value)

        for item in all_houses_dic.values():
            for house in item:
                all_houses_new, total_value = swap_houses(house=house, all_houses=all_houses_dic, waters=waters, total_value_map=total_value, algoritme=0)

        print(total_value)
        visualisation(all_houses=all_houses_new, waters=waters) 
        visualisation_plot()

        for item in all_houses_new.values():
            for house in item:
                all_houses, total_value = swap_houses(house=house, all_houses=all_houses_dic, waters=waters, total_value_map=total_value, algoritme=algoritme)
            
        all_houses_dic = copy.deepcopy(all_houses)
    
    return total_value, all_houses_dic, waters