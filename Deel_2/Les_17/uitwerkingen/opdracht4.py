import random

aantal_rondes = 0
aantal_fouten = 0

while True:
    random_getal = random.randint(1, 5)
    aantal_rondes += 1

    while True:
        ingevoerd_getal = int(input("Raad het getal tussen 1 en 5: "))

        if ingevoerd_getal == random_getal:
            print(" hebt het getal goed geraden! ")  
            break
        else:
            print(" hebt het getal niet goed geraden. Probeer opnieuw. ")  
            aantal_fouten += 1

    opnieuw_spelen = input("Wil je nog een ronde spelen? (ja/nee): ").lower()
    if opnieuw_spelen != "ja":
        break

print("Aantal gespeelde rondes:", aantal_rondes)
print("Aantal keer fout geraden:", aantal_fouten)
