import math

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
        self.added_value = None
        self.total_price = None
        self.shortest_distance = None

    def location(self, bottom_left):
        self.bottom_left = bottom_left
        self.bottom_right = ((bottom_left[0] + self.width), bottom_left[1]) 
        self.top_left = (bottom_left[0], (bottom_left[1] + self.length))
        self.top_right = ((bottom_left[0] + self.width), (bottom_left[1] + self.length))
    
    def compared_space(self, neighbour, distance):
        '''Berekend de afstand tot andere huizen die al zijn geplaatst en slaat deze afstand op'''
        self.neighbours[neighbour.name] = math.floor(distance)

    def extra_meters(self):
        shortest_distance = 241 #maximale afstand totale kaart
        object_shortest_distance = None

        for tuples in self.neighbours.items():
            if tuples[1] < shortest_distance:
                shortest_distance = tuples[1]
                object_shortest_distance = tuples[0]
        
        self.shortest_distance = math.floor(shortest_distance)

        self.extra_space = shortest_distance - self.obligated_space
        
    
    def totalprice(self):
        total_rate = (self.rate * self.extra_space) + 1
        self.total_price = self.start_value * total_rate
        return self.total_price

    def addedvalue(self):
        self.added_value = total_price - start_value
        return self.added_value

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
