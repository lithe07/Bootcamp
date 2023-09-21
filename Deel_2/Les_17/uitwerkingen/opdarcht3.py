import random

aantal_rondes = 3

for ronde in range (aantal_rondes):
    random_getal = random.randint(1, 5)

    while True:
        ingevoerd_getal = int(input("Raad het getal tussen 1 en 5: "))

        if ingevoerd_getal == random_getal:
            print("je hebt het getal goed geraden")
            break
        else:
            print("je hebt het getal niet goed geraden")

    print("ronde", ronde + 1,"is voorbij. het juiste getal was:", random_getal)