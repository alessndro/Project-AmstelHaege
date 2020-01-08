class House:
    def __init__(self, size, start_value, obligated_space, rate, length, width):
        self.size = size
        self.start_value = start_value
        self.obligated_space = obligated_space
        self.min_extra_space = min_extra_space
        self.rate = rate
        self.length = length
        self.width = width
        self.placed = placed

    def location(self, bottom_left):
        self.bottom_left = bottom_left
        self.bottom_right = ((bottom_left[0] + width), bottom_left[1]) 
        self.top_left = (bottom_left[0], (bottom_left[1] + length))
        self.top_right = ((bottom_left[0] + width), (bottom_left[1] + length))
        return (bottom_left, top_right)

    def extra_space(self):
        pass
    
    def totalprice(self, extra_meters):
        total_rate = self.rate * extra_meters + 1
        self.total_price = self.start_value * total_rate
        return self.total_price

    def addedvalue(self):
        self.added_value = total_price - start_value
        return self.added_value


class Water:
    def __init__(self, size, top_right, top_left, bottom_right, bottom_left):
        self.size = size
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right
