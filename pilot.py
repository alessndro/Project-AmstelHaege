from matplotlib import pyplot as plt 

def visualisation(all_houses, waters):

    plt.xlabel('in meters')
    plt.ylabel('in meters')
    plt.title('map')
    plt.axis([0, 160, 0, 180])
    ground = plt.Rectangle((0,0), 160, 180, fc='green')      
    plt.gca().add_patch(ground)
    for water in waters:
        print(water.map)
        print(water.bottom_left)
        water = plt.Rectangle((water.bottom_left), water.bottom_right[0] - water.bottom_left[0], water.top_right[1] - water.bottom_left[1], fc='blue') 
        plt.gca().add_patch(water) 
   
    for key in all_houses.values():
        for house in key: 
            if house.size == "small":
                rectangle = plt.Rectangle(house.bottom_left, 10, 10, fc='pink',ec="red", linewidth=2)
            if house.size == "medium":
                rectangle = plt.Rectangle(house.bottom_left, 14, 10, fc='purple',ec="red", linewidth=3)
            if house.size == "large":
                rectangle = plt.Rectangle(house.bottom_left, 18, 16, fc='black',ec="red", linewidth=6)       
            plt.gca().add_patch(rectangle)
    plt.show()
