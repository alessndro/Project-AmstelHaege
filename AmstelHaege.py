from models import House, Water
from random import seed
from random import random
import _random
import math

def main():
    
    # Daniel wil seed later gebruiken, zorgt voor zelfde uitkomst okal random
    # Kiara wil math.floor verwijderen voor exacte cordinaten ipv grid
    # Alessandro wilt niks
    # seed()
    random_x = math.floor(random()*160)
    random_y = math.floor(random()*180)
    print(random_x)
    print(random_y)

if __name__ == "__main__":
    main()


