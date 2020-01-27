from models import House, Water
from random import seed
from algorithms import *
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
        number_of_houses = int(input("What are the amount of Houses 20, 40 or 60?"))

        map_number = int(input("Which map would you like to use? 1,2,3"))

        algoritme = int(input("Which algorithm would you like to use?  press 1 for random algorithm, 2 for ascending hillclimber, 3 for greedy, 4 for swappinghouses, 5 for double random"))
        
        # als de juiste waarden worden gekozen, begin het programma
        if (number_of_houses == 20 or number_of_houses == 40 or number_of_houses == 60) and (map_number > 0 and map_number <= 3) and algoritme > 0 and algoritme < 7:
            break
        
    return number_of_houses, map_number, algoritme

def random(number_of_houses, map_number, turns):
    ''' zorgt ervoor dat het random algorite x aantal keer wordt uitgevoerd '''
    total_value_map = 0
    for i in range(turns):
        # voert het algoritme uit
        all_houses, total_value, waters = random_algoritme(number_of_houses, map_number)
        # houdt elke run van het algoritme bij, en de uitkomsten hiervan
        write_progress(number_of_houses=number_of_houses, map_number=map_number, solution=count, total_value_map=total_value)
        # schrijft de resultaten van deze run op om dit te kunnen plotten
        write_progress_run(number_of_houses=number_of_houses, map_number=map_number, solution=count, total_value_map=total_value)
        # als de waarde hoger is dan de vorige waarde, sla deze op als nieuwe waarde
        if total_value > total_value_map:
            total_value_map = total_value
            all_houses_dic = copy.deepcopy(all_houses)
    
    return total_value, all_houses_dic, waters 
        
def asceding_hillclimber_algoritme(number_of_houses, map_number, all_houses, waters, total_value_map):
    ''' zorgt ervoor dat er een ascending hillclimber wordt uitgevoerd '''
    if algoritme == 2:
        # plaatst alle huizen random op de kaart
        all_houses, total_value, waters = random_algoritme(number_of_houses, map_number)
        
        # verplaatst alle huizen, probeert elke mogelijke plek uit en bewaard de beste positie waarmee de waarde van de kaart hoger is
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

    # loop door alle huizen en plaats deze op de meest gunstige plek zodat de waarde van de kaart het hoogst is
    for house in all_houses_dic["large"]:
        all_houses_dic, total_value = greedy_algoritme(house, all_houses_dic, waters)

    for house in all_houses_dic["medium"]:
        all_houses_dic, total_value = greedy_algoritme(house, all_houses_dic, waters)

    for house in all_houses_dic["small"]:
            all_houses_dic, total_value = greedy_algoritme(house, all_houses_dic, waters)

    
    return total_value, all_houses_dic, waters

def swapping_houses_algoritme(number_of_houses, map_number, all_houses, waters, total_value_map, algoritme):
    ''' plaatst de huizen random, en swapt vervolgens de huizen met elkaar om te kijken of
        dit een hogere waarde zal opleveren (all_houses en waters worden meegegeven voor algoritme nummer 6) '''

    # plaatst de huizen random
    if algoritme == 4:
        all_houses, total_value, waters = random_algoritme(number_of_houses, map_number)

    # roept het algoritme aan voor het swappen van de huizen
    for item in all_houses.values():
        for house in item:
            all_houses_new, total_value = swap_houses(house=house, all_houses=all_houses, waters=waters, total_value_map=total_value_map)
        
        all_houses_dic = copy.deepcopy(all_houses_new)

    return total_value, all_houses_dic, waters

def random_ascending_hillclimber_algoritme(number_of_houses, map_number):
    ''' plaatst alle huizen op een random locatie, en zoekt dan per huis 10 random nieuwe locaties en kijkt of hiermee de waarde van de map te verhogen is '''

    # plaatst alle huizen op een random locatie
    all_houses, total_value, waters = random_algoritme(number_of_houses, map_number)

    # roept random hillclimber aan, deze pakt een bestaand huis, en kijkt voor 10 nieuwe punten wat de beste plek zou zijn om dit huis te plaatsen
    for item in all_houses.values():
        for house in item:
            all_houses_new, total_value = random_ascending_hillclimber(house=house, all_houses=all_houses, waters=waters, total_value_map=total_value)
    all_houses_dic = copy.deepcopy(all_houses_new)
    
    return total_value, all_houses_dic, waters

def swap_houses_after_greedy_algoritme(number_of_houses, map_number, all_houses, waters, total_value_map, algoritme):

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

        # loop door alle huizen en plaats deze op de meest gunstige plek volgens het greedy algoritme
        for house in all_houses_dic["large"]:
            all_houses_dic, total_value = greedy_algoritme(house, all_houses_dic, waters)

        for house in all_houses_dic["medium"]:
            all_houses_dic, total_value = greedy_algoritme(house, all_houses_dic, waters)

        for house in all_houses_dic["small"]:
            all_houses_dic, total_value = greedy_algoritme(house, all_houses_dic, waters)

        # swap de huizen om een hogere totale waarde te krijgen
        for item in all_houses_dic.values():
            for house in item:
                all_houses_new, total_value = swap_houses(house=house, all_houses=all_houses_dic, waters=waters, total_value_map=total_value, algoritme=0)

        for item in all_houses_new.values():
            for house in item:
                all_houses, total_value = swap_houses(house=house, all_houses=all_houses_dic, waters=waters, total_value_map=total_value, algoritme=algoritme)
            
        all_houses_dic = copy.deepcopy(all_houses)
    
        return total_value, all_houses_dic, waters