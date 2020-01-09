from matplotlib import pyplot as plt 


# rectangle = plt.Rectangle((0,0), 20, 20, fc='blue',ec="red")
# plt.gca().add_patch(rectangle)
# plt.axis('scaled')

# wat heb je nodig
# map number voor water

#def visualisation(map_number, all_houses):
# for size in all_houses:
    # for house in size:
        # doe de visualisatie hieronder

#for house in list_of_houses:
plt.xlabel('in meters')
plt.ylabel('in meters')
plt.title('map')
plt.axis([0, 160, 0, 180])
ground = plt.Rectangle((0,0), 160, 180, fc='green')      
water = plt.Rectangle((0,0), 32, 180, fc='blue',ec="blue") 
plt.gca().add_patch(ground)
plt.gca().add_patch(water) 
for i in range(3):
    #if house.size == "small":
        #rectangle = plt.Rectangle(house.bottem_left, 10, 10, fc='pink',ec="red")
    #if house.size == "medium":
        #rectangle = plt.Rectangle(house.bottem_left, 14, 10, fc='purple',ec="red")
    #if house.size == "large":
        #rectangle = plt.Rectangle(house.bottem_left, 18, 16, fc='red',ec="red")       
    rectangle = plt.Rectangle((30 +2 * i,0+32*i), 30, 20, fc='black',ec="red", linewidth=6)
    plt.gca().add_patch(rectangle)

    
plt.show()
