lijst = [1, 2, 3, 4, 5]

index = int(input("voer index tusseen 0, 4: "))
if index >=  0 and index < len(lijst):
    getal_verwijderen = lijst.pop(index)
    print(lijst)
    print(getal_verwijderen)