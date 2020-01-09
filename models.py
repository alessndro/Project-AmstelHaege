class House:
    def __init__(self, name, size, start_value, obligated_space, rate, length, width):
        self.name = name
        self.size = size
        self.start_value = start_value
        self.obligated_space = obligated_space
        self.min_extra_space = min_extra_space
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

    def location(self, bottom_left):
        self.bottom_left = bottom_left
        self.bottom_right = ((bottom_left[0] + width), bottom_left[1]) 
        self.top_left = (bottom_left[0], (bottom_left[1] + length))
        self.top_right = ((bottom_left[0] + width), (bottom_left[1] + length))
    
    def compared_space(self, neighbor)
        '''Berekend de afstand tot andere huizen die al zijn geplaatst en slaat deze afstand op'''
        neighbors = {}

        #FUNCTIE AFSTAND BEREKENEN TOT ANDER HUIS
        
        neighbors[neighbor] = afstand
        pass

    def extra_space(self):
        # bereken kortste afstand tot volgende huis, bereken of dit groter is dan de minimale vereisten
        pass
        
    
    def totalprice(self, extra_meters):
        total_rate = self.rate * extra_meters + 1
        self.total_price = self.start_value * total_rate
        return self.total_price

    def addedvalue(self):
        self.added_value = total_price - start_value
        return self.added_value

    def __str__(self):
        return (self.name, self.size, self.placed, self.total_price)


class Water:
    def __init__(self, size, top_right, top_left, bottom_right, bottom_left):
        self.size = size
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right
