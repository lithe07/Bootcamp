naam = input("wat is u naam?")
kleuren = ("rood", "Blauw", "Groen", "zwaart")

favoriete_kleur = input("wat is jouw favoriete kleur?")

if favoriete_kleur.lower() in kleuren:
    print(f"{naam}, je favoriete kleur, {favoriete_kleur}, is gewildig!")
else:
    print("Deze kleur is niet zo gewildig!")
