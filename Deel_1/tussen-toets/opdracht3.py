naam = input("wat is u naam?")
leeftijd = int(input("wat is u leeftijd?"))

if leeftijd < 18:
    print(f"best {naam}, je bent nog geen 18. Alleen autorijden zit er dus niet in")
else:
    print(f"Beste {naam}, je bent 18 of ouder en mag dus alleen autorijden (met rijbewijs althans).")


