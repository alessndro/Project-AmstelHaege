import csv

def write_solution_down(total_value_map, all_houses, number_of_houses, all_water_objects, chosen_map, algoritme):
    solution_twenty = 0
    solution_fourty = 0
    solution_sixty = 0
    count = 0
    with open('solution.csv', 'r', newline='') as file:
        reader = csv.reader(file)

        for line in reader:
            
            if line[1] == chosen_map and line[3] == number_of_houses and line[5] < total_value_map and line[7] == algoritme
        
        with open('temp_solution', 'w') as output:
            writer = csv.writer(output)




        writer = csv.writer(file)

        write.writerow(["map:", chosen_map, "number of houses", number_of_houses,
                        "total value: ", total_value_map, "algoritme: ", algoritme)
        for item in all_houses.values():
            for house in item:
                write.writerow([])
                                    (
            writer.writerow([house.name, house.size, house.bottem_left, house.top_right])


# def read_previous_solutions(chosen_map, number_of_houses):
    
#     highest_total_value_map = 0
#     solution = -1
#     with open ('progress.csv', 'r') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             if chosen_map == row[1] and number_of_houses == row[0]:
#                 if row[3] > highest_total_value_map
#                 highest_total_value_map = row[3]
#                 solution = row[2]

#     reader.close()
#     return highest_total_value_map, solution

def write_progress(number_of_houses, solution, map_number, total_value_map, all_houses):

    with open('progress.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        writer.writerow([number_of_houses, map_number, solution, total_value_map])
        for item in all_houses.values():
            for house in item:
                writer.writerow([house.name, house.size, house.bottem_left, house.top_right])


##############################################################################################
# VOOR ELKE RUN 
##############################################################################################
def write_progress_run(number_of_houses, map_number, solution, total_value_map):
    
    with open('progress_run.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        writer.writerow([number_of_houses, map_number, solution, total_value_map])

def read_progress_run():
    
    x = []
    y = []

    with open('progress_run.csv', 'r') as file:
        reader = csv.reader(file)

        for line in reader:
            x.append(line[2]) 
            y.append(line[3])

    return x, y

    
def delete_progress_run():
    lines = []
    with open('progress_run.csv', 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            pass
            
    with open('progress_run.csv', 'w') as file:

        writer = csv.writer(file)

        writer.writerows(lines)
            

    



            