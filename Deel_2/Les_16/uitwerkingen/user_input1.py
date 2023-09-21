def get_integer(Vraag):
    while True:
        getal = int(input(Vraag))
        try:
            return getal
        except ValueError:
            print("ongelidig invoer. voer een geldig interger in.")

def get_float(prompt):
    while True:
        getal1 = float(input(prompt))
        try:
            return getal1
        except ValueError:
            print("ongeldig invoer. voer een geldig gloat in ")

def get_string(prompt):
    zin = str(input(prompt))
    return zin

def get_letter(prompt):
    while True:
        letter_input = input(prompt)
        if len(letter_input) == 1:
            return letter_input.upper()
        else:
            print("voer een letter in aub")