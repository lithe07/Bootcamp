naam = ["Lithe, Osama, Rando, Oskar, Amasia"]
naam_vragen = input("voeg naam toe !")

if naam_vragen in naam:
    naam.remove(naam_vragen)
    print(f"{naam_vragen} is verwijderd uit de lijst. ")
else:
    naam.append(naam_vragen)
    print(f"{naam_vragen} is toevoegd aan de lijst")

print("bijgewerkte lijst van naam")
print(naam)
