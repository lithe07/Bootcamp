fruiten_lijst = ["druiven", "sinasapple", "banan"]

fruit = input("voer een soort fruit in? ")
if fruit in fruiten_lijst:
    fruiten_lijst.remove(fruit)
    print(fruit)
    print(fruiten_lijst)
else: 
    print("fout melding! ")
