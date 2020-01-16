from matplotlib import pyplot as plt 

def visualisation(all_houses, waters):

    plt.xlabel('in meters')
    plt.ylabel('in meters')
    plt.title('map')
    plt.axis([0, 160, 0, 180])
    ground = plt.Rectangle((0,0), 160, 180, fc='forestgreen')      
    plt.gca().add_patch(ground)
    for water in waters:
        water = plt.Rectangle((water.bottom_left), water.bottom_right[0] - water.bottom_left[0], water.top_right[1] - water.bottom_left[1], fc='blue') 
        plt.gca().add_patch(water) 
   
    for key in all_houses.values():
        for house in key: 
            if house.size == "small":
                rectangle = plt.Rectangle(house.bottom_left, 8, 8, fc='purple',ec="green", linewidth=2)
            if house.size == "medium":
                rectangle = plt.Rectangle(house.bottom_left, 11, 7, fc='yellow',ec="green", linewidth=3)
            if house.size == "large":
                rectangle = plt.Rectangle(house.bottom_left, 12, 10, fc='red',ec="green", linewidth=6)       
            plt.gca().add_patch(rectangle)
    plt.show()
