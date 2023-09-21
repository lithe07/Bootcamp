import random

random_getal = random.randint(0,1)


ingevoerd_getal = int(input("Raad het getal tussen 1 en 5: "))


if ingevoerd_getal == random_getal:
    print("\033[32mJe hebt het getal goed geraden!\033[0m")  
else:
    print("\033[31mJe hebt het getal niet goed geraden!\033[0m")  
