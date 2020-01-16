import matplotlib.pyplot as plt
import csv



def read_progress_run():
    
    x = []
    y = []

    with open('progress_run.csv', 'r') as file:
        reader = csv.reader(file)

        for line in reader:
            x.append(line[2]) 
            y.append(line[3])

    print(x)
    print(y)
    plt.plot(x, y, color='black', marker='o')        
    plt.title('Returns of number_of_houses houses in map map_number', fontsize=15)
    plt.xlabel('Count', fontsize=11)
    plt.ylabel('Total value', fontsize=11)
    plt.grid(True)
    plt.show()