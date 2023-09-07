cijfer = int(input("voer een cijfer in tussen 1 en 10: "))

if cijfer >= 1 and cijfer <= 10:
    omschrijvingen = {
    10: "uitmuntend",
    9: "zeer goed",
    8: "goed",
    7: "ruim voldoende",
    6: "voldoende",
    5: "bijna voldoende",
    4: "onvoldoende",
    3: "gering",
    2: "slecht",
    1: "zeer slecht",
}
    omschrijvingen = omschrijvingen[cijfer]
    if cijfer >= 6:
        print(f"Gefeliciteerd,{omschrijvingen}, je resultaat is een {cijfer}. ")
    else:
        print(f"jammer,{omschrijvingen}, je resultaat is een {cijfer}.")
else:
    print("Dit kan ik niet omzetten! voer een cijfer tussen 1 een 10 in.")