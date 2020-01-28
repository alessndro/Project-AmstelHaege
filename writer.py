#########################################################################
# writer.py
#
# Minor Programming 
#
# Kiara Shakira, Sander van bergen, Daniel Siha
#
# Bevat alle functies voor het schrijven van resultaten
##########################################################################

import csv

def write_progress(number_of_houses, solution, map_number, total_value_map, all_houses):
    ''' Schrijft slaat het resultaat van de run op in progress file  '''

    # open file
    with open('progress.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        # noteer alle resultaten in het file 
        writer.writerow([number_of_houses, map_number, solution, total_value_map])
        for item in all_houses.values():
            for house in item:
                writer.writerow([house.name, house.size, house.bottem_left, house.top_right])

def write_progress_run(number_of_houses, map_number, solution, total_value_map):
    ''' Noteert de resultaten van de huidige run '''
    
    with open('progress_run.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        writer.writerow([number_of_houses, map_number, solution, total_value_map])

def read_progress_run():
    ''' leest alle waardes uit progress_run file en slaat deze op in een x en y as lijst '''
    
    x = []
    y = []

    with open('progress_run.csv', 'r') as file:
        reader = csv.reader(file)

        for line in reader:
            x.append(line[2]) 
            y.append(line[3])

    return x, y

    
def delete_progress_run():
    ''' verwijderd alle data uit progress_run document '''
    lines = []
    with open('progress_run.csv', 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            pass
            
    # overschrijft alle informatie in progress_run en maakt vult deze met een lege lijst
    with open('progress_run.csv', 'w') as file:

        writer = csv.writer(file)

        writer.writerows(lines)
            

    



            