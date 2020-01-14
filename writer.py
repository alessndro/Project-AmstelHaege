
import csv

def write_solution_down(total_value_map, all_houses, number_of_houses, all_water_objects, chosen_map):
    solution_twenty = 0
    solution_fourty = 0
    solution_sixty = 0
    with open('solution.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        if number_of_houses == 20:
            for size in all_houses:
                for house in size:
                    write.writerow(["map:", chosen_map, "number of houses", number_of_houses,
                                    "solution:", solution_twenty, "size house: ", house.size, "coordinates: ", house.coordinates,
                                    "extra_space: ", house.extra_space])
            write_progress(number_of_houses, solution_twenty, total_value_map)

        if number_of_houses == 40:
            for size in all_houses:
                for house in size:
                    write.writerow(["map:", chosen_map, "number of houses", number_of_houses,
                                    "solution:", solution_fourty, "size house: ", house.size, "coordinates: ", house.coordinates,
                                    "extra_space: ", house.extra_space])
            write_progress(number_of_houses, solution_twenty, total_value_map)
                    
        if number_of_houses == 60:
            for size in all_houses:
                for house in size:
                    write.writerow(["map:", chosen_map, "number of houses", number_of_houses,
                                    "solution:", solution_sixty, "size house: ", house.size, "coordinates: ", house.coordinates,
                                    "extra_space: ", house.extra_space])
            write_progress(number_of_houses, solution_twenty, total_value_map)

        write.writerow(["Total value solution = ", total_value_map])
    writer.close()

def read_previous_solutions(chosen_map, number_of_houses):
    
    highest_total_value_map = 0
    solution = -1
    with open ('progress.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if chosen_map == row[1] and number_of_houses == row[0]:
                if row[3] > highest_total_value_map
                highest_total_value_map = row[3]
                solution = row[2]

    reader.close()
    return highest_total_value_map, solution

def write_progress(number_of_houses, solution, total_value_map):

    with open('progress.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        if number_of_houses == 20:
            write.writerow([number_of_houses, chosen_map, solution, total_value_map])
        if number_of_houses == 40:

        if number_of_houses == 60:
    writer.close()


def delete_previous_solution():
    pass



              # onder
                if placed_house.bottom_left[1] <= selected_house.bottom_left[1] and (selected_house.top_left[0] <= placed_house.bottom_left[0] <= selected_house.top_right[0] or selected_house.top_left[0] <= placed_house.bottom_right[0] <= selected_house.top_right[0]):

                    distance = selected_house.bottom_left[1] - placed_house.top_left[1]
                # boven
                elif placed_house.bottom_right[1] >=  selected_house.top_right[1] and (selected_house.bottom_left[0] <= placed_house.bottom_right[0] <= selected_house.bottom_right[0] or selected_house.bottom_left[0] <= placed_house.bottom_left[0] <= selected_house.bottom_right[0]):

                    distance = placed_house.bottom_right[1]-selected_house.top_right[1]
                #links
                elif placed_house.bottom_right[0] <= selected_house.bottom_left[0] and (selected_house.bottom_left[1] <= placed_house.bottom_right[1] <= selected_house.top_left[1] or selected_house.bottom_left[1] <= placed_house.top_right[1] <= selected_house.top_left[1]):
                    distance = selected_house.bottom_left[0]-placed_house.bottom_right[0]
                #rechts
                elif placed_house.bottom_right[0] >= selected_house.bottom_left[0] and (selected_house.bottom_left[1] <= placed_house.bottom_right[1] <= selected_house.top_left[1] or selected_house.bottom_left[1] <= placed_house.top_right[1] <= selected_house.top_left[1]):
                    distance = placed_house.bottom_right[0] - selected_house.bottom_left[0]
                # linksboven 
                elif selected_house.top_left[0] > placed_house.bottom_right[0] and selected_house.top_left[1] < placed_house.bottom_right[1]:
                    delta_x_sq = (selected_house.top_left[0]-placed_house.bottom_right[0])**(2)
                    delta_y_sq = (placed_house.bottom_right[1]-selected_house.top_left[1])**(2)
                    distance = math.sqrt(delta_x_sq + delta_y_sq)
                    # distance = math.sqrt(((selected_house.top_left[0]-placed_house.bottom_right[0])**(2))+((placed_house.bottom_right[1]-selected_house.top_left[1])**(2)))
                # rechtsboven
                elif selected_house.top_right[0] < placed_house.bottom_left[0] and selected_house.top_right[1] < placed_house.bottom_left[1]:
                    delta_x_sq = (placed_house.bottom_left[0]-selected_house.top_right[0])**(2)
                    delta_y_sq = (placed_house.bottom_left[1]-placed_house.top_right[1])**(2)
                    distance = math.sqrt(delta_x_sq + delta_y_sq)
                    # distance = math.sqrt((placed_house.bottom_left[0]-selected_house.top_right[0])**(2))+((placed_house.bottom_left[1]-placed_house.top_right[1])**(2))
                # rechtsonder
                elif selected_house.bottom_right[0] < placed_house.top_left[0] and selected_house.bottom_right[1] > placed_house.top_left[1]:
                    delta_x_sq = (placed_house.top_left[0]-selected_house.top_right[0])**(2)
                    delta_y_sq = (selected_house.bottom_right[1]-selected_house.top_left[1])**(2)
                    distance = math.sqrt(delta_x_sq + delta_y_sq)
                    # distance = math.sqrt((placed_house.top_left[0]-selected_house.top_right[0])**(2))+((selected_house.bottom_right[1]-selected_house.top_left[1])**(2))
                # linksonder
                elif selected_house.bottom_left[0] > placed_house.top_right[0] and selected_house.bottom_left[1] > placed_house.top_right[1]:
                    delta_x_sq = (selected_house.bottom_left[0]-placed_house.top_right[0])**(2)
                    delta_y_sq = (selected_house.bottom_left[1]-placed_house.top_right[1])**(2)
                    distance = math.sqrt(delta_x_sq + delta_y_sq)
                    # distance = math.sqrt(((selected_house.bottom_left[0]-placed_house.top_right[0]**(2))+((selected_house.bottom_left[1]-placed_house.top_right[1])**(2))))

                else:
                    distance = 0
                    print("9")
                    print(selected_house, placed_house)
                selected_house.compared_space(placed_house, distance)
                # EXTRA CONTROLE TOEVOEGEN
                pass