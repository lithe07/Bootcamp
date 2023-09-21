import random

aantal_rondes = 0
aantal_fouten = 0

def is_geldig_getal(getal):
    return 1 <= getal <= 5  

while True:
    random_getal = random.randint(1, 5)
    aantal_rondes += 1

    while True:
        ingevoerd_getal = int(input("Raad het getal tussen 1 en 5: "))
        
        if is_geldig_getal(ingevoerd_getal):
            break
        else:
            print("Ongeldig getal. Voer een getal tussen 1 en 5 in.")

    while True:
        ingevoerd_getal = int(input("Raad het getal tussen 1 en 5: "))

        if is_geldig_getal(ingevoerd_getal):
    
            if ingevoerd_getal == random_getal:
                print("\033[32mJe hebt het getal goed geraden!\033[0m")
                break
            else:
                print("\033[31mJe hebt het getal niet goed geraden. Probeer opnieuw.\033[0m") 
                aantal_fouten += 1
        else:
            print("Ongeldig getal. Voer een getal tussen 1 en 5 in.")

    opnieuw_spelen = input("Wil je nog een ronde spelen? (ja/nee): ").lower()
    if opnieuw_spelen != "ja":
        break

print("Aantal gespeelde rondes:", aantal_rondes)
print("Aantal keer fout geraden:", aantal_fouten)
