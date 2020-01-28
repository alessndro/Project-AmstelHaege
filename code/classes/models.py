#########################################################################
# classes.py
#
# Minor programmeren
#
# Kiara Evers, Alessandro Degenkamp, Daniel Siha
#
# Bevat alle classes die worden gebruikt in dit project
##########################################################################

import math
import time

# constante
MAXIMALE_AFSTAND_KAART = 241

class House:
    def __init__(self, name, size, start_value, obligated_space, rate, length, width):
        self.name = name
        self.size = size
        self.start_value = start_value
        self.obligated_space = obligated_space
        self.rate = rate
        self.length = length
        self.width = width
        self.placed = False
        self.bottom_left = None
        self.bottom_right = None
        self.top_right = None
        self.top_left = None
        self.total_value = None
        self.extra_space = 0 
        self.neighbours = {}
        self.total_price = None
        self.shortest_distance = None

    def location(self, bottom_left):
        ''' Berekent de overige coördinaten op basis van de gegeven bottom_left
         en de waardes die het huis heeft gekregen bij het aanmaken van het object '''
        self.bottom_left = bottom_left
        self.bottom_right = ((bottom_left[0] + self.width), bottom_left[1]) 
        self.top_left = (bottom_left[0], (bottom_left[1] + self.length))
        self.top_right = ((bottom_left[0] + self.width), (bottom_left[1] + self.length))
    
    def compared_space(self, neighbour, distance):
        ''' Berekent de afstand tot andere huizen die al zijn geplaatst en slaat deze afstand op '''
        self.neighbours[neighbour.name] = math.floor(distance)

    def extra_meters(self):
        ''' Bekijkt welke afstand van de geregisteerde afstanden de kortste is en berekent 
        daarmee hoeveel meer vrijstand de woning heeft '''
        shortest_distance = MAXIMALE_AFSTAND_KAART
        object_shortest_distance = None

        # slaat de korste afstand op 
        for tuples in self.neighbours.items():
            if tuples[1] < shortest_distance:
                shortest_distance = tuples[1]
                object_shortest_distance = tuples[0]
        
        # berekent hoeveel afstand er over is naast de verplichte vrijstand
        self.shortest_distance = math.floor(shortest_distance)

        self.extra_space = shortest_distance - self.obligated_space
        
    
    def totalprice(self):
        ''' Berekent de totale waarde van de woning met de extra vrijstand die de woning heeft '''
        total_rate = (self.rate * self.extra_space) + 1
        self.total_price = self.start_value * total_rate
        return self.total_price

    def __str__(self):
        return f"{self.name}, {self.size}, {self.placed} {self.bottom_left}"


class Water:
    def __init__(self, map, top_right, top_left, bottom_right, bottom_left):
        self.map = map
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right

    def __str__(self):
        return f"{self.map, self.bottom_right}"
    