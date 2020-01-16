from matplotlib import pyplot as plt 
from writer import read_progress_run, delete_progress_run


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


def visualisation_plot():

    x, y = read_progress_run()

    plt.plot(x, y, color='black', marker='o')        
    plt.title('Returns of number_of_houses houses in map map_number', fontsize=15)
    plt.xlabel('Count', fontsize=11)
    plt.ylabel('Total value', fontsize=11)
    plt.grid(True)
    plt.show()

    delete_progress_run()