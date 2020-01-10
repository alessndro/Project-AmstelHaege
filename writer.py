
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
                                    "solution number:", solution_sixty, "size house: ", house.size, "coordinates: ", house.coordinates,
                                    "extra_space: ", house.extra_space])
            write_progress(number_of_houses, solution_twenty, total_value_map)

        write.writerow(["Total value solution = ", total_value_map])
    writer.close()

def read_previous_solutions(chosen_map, number_of_houses):
    
    with open ('progress.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            pass

    return highest_total_value_map

def write_progress(number_of_houses, solution, total_value_map):

    with open('progress.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        if number_of_houses == 20:
            write.writerow([solution, total_value_map])
    writer.close()


def delete_previous_solution():
    pass

