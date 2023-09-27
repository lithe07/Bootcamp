# opdrach 1:
# a. je kan de fout en je code makkelijk zien en hijn geeft aan waar precies de fout ligt. afkortingen in codes
# b. zodat je makkelijk kan terug kijken naar je code jij of iemand anders die wilt mee kijken 

# opdracht 2:
# Maak het commentaar af.
a = 5  # dit is een voorbeeld van het datatype: geheel getal zonder komma
b = 10.5# dit is een voorbeeld van het datatype: kommagetal
c = "Hallo wereld" # dit is een voorbeeld van het datatype: een tekst

# opdracht 3:
a = 5
b = 10

wissel = a
a = b 
b = wissel

print(f"a = {a}, b = {b}") 

# opdracht 4
leeftijd = int(input("Hoe oud ben je? "))
print(f"Dan duurt het nog ongeveer {67 - leeftijd} jaar voordat je met pensioen mag!")


# Opdracht 5: 
def som(a, b, c):
    return a + b + c

getal1 = 200
getal2 = 5
getal3 = 12
antwoord = som(getal1, getal2, getal3)

print(f"De som van {getal1} + {getal2} + {getal3} = {antwoord}")

# opdrach 6
AANTAL_GB = 20
AANTAL_MINUTEN = 200 
ONBEPERKT = False 
aantal_minuten_gebeld = int(input("Hoeveel minuten heb je gebeld?"))
aantal_GB_internet = int(input("Hoeveel GB's heb je gebruikt?"))


if not ONBEPERKT and aantal_minuten_gebeld > AANTAL_MINUTEN or aantal_GB_internet > AANTAL_GB :
    print("Let op: je moet bijbetalen!")

    

else:
    print("Niet aan de hand gebruik je mobiel lekker verder!")


# opdarcht 7
for x in range(1, 251): 
    print(x)


# Opdracht 8:
lijst_eten = ['appel', 'pannenkoek', 'kiwi', 'hamburger']


print("Onze menukaart:")
for gerecht in lijst_eten:
    print(gerecht)


langste_naam = max(lijst_eten, key=len)
print(f"\nHet eten met de langste naam op het menu is: {langste_naam}")


#opdracht 9
while True:
    try:
        cijfer = float(input("voer een cijfer tussen 0 en 10 in: "))
        if 0 <= cijfer <= 10:
            print("goed gedaan! het ingevoerde cijfer is gedlig. ")
            break
        else:
            print("fout! het ingevoerde cijfer moet tussen 0 en 10 liggen ")
    except ValueError:
        print("fout! voer aub een geldig getal in. ")

# opdarcht 10
MAX = 20
getal = int(input("Voer een getal in"))

if getal > MAX:
    print(f"Het getal is groter dan {MAX}")
elif getal < MAX:
    print(f"Het getal is kleiner dan {MAX}")
else:
    print(f"Het getal is gelijk aan {MAX}")
