import random

random_getal = random.randint(1, 5)

pogingen = 0  

while True:
    ingevoerd_getal = int(input("Raad het getal tussen 1 en 5: "))
    
    if ingevoerd_getal == random_getal:
        print("\033[32mJe hebt het getal goed geraden na" "pogingen!\033[0m")  
        break
    else:
        print("\033[31mJe hebt het getal niet goed geraden. Probeer opnieuw.\033[0m") 
