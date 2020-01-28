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

def write_progress(number_of_houses, map_number, total_value_map, all_houses):
    ''' Schrijft slaat het resultaat van de run op in progress file  '''

    # open file
    with open('solutions.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        # noteer alle resultaten in het file 
        writer.writerow([number_of_houses, map_number, total_value_map])
        for item in all_houses.values():
            for house in item:
                writer.writerow([house.name, house.size, house.bottom_left, house.top_right])

def write_progress_run(number_of_houses, map_number, total_value_map):
    ''' Noteert de resultaten van de huidige run '''
    
    with open('progress_run.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        writer.writerow([number_of_houses, map_number, total_value_map])

def read_progress_run():
    ''' leest alle waardes uit progress_run file en slaat deze op in een x en y as lijst '''
    
    x = []
    y = []

    with open('progress_run.csv', 'r') as file:
        reader = csv.reader(file)

        for line in reader:
            # slaat het map number op
            x.append(line[1]) 
            # slaat de totale waarde op
            y.append(line[2])

    return x, y

    
def delete_progress_run():
    ''' verwijderd alle data uit progress_run document '''
    lines = []
    with open('progress_run.csv', 'r') as file:
        reader = csv.reader(file)

    # overschrijft alle informatie in progress_run en maakt vult deze met een lege lijst
    with open('progress_run.csv', 'w') as file:

        writer = csv.writer(file)

        writer.writerows(lines)
            
    
