class House:
    def __init__(self, size, start_value, obligated_space, min_extra_space,
    	    rate, top_left, top_right, bottom_right, bottom_left, total_price):
        self.size = size
        self.start_value = start_value
        self.obligated_space = obligated_space
        self.min_extra_space = min_extra_space
        self.rate = rate
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right
        self.total_price = total_price

class Water:
    def __init__(self, size, top_right, top_left, bottom_right, bottom_left):
        self.size = size
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right
