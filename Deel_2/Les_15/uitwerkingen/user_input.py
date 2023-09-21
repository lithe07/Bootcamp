def get_integer(Vraag):
    getal = int(input(Vraag))
    return getal

def get_float(prompt):
    getal1 = float(input(prompt))
    return getal1

def get_string(prompt):
    zin = str(input(prompt))
    return zin

def get_letter(prompt):
    while True:
        letter_input = input(prompt)
        if len(letter_input) == 1:
            return letter_input.upper()
        else:
            print("voer een letter in ya eri")

#  vraagt de gebruiker een getal in te voeren 
#  def get_intger(vraag):
#      while True:
#     try:
#         getal = int(input(vraag))
#         break
#     except ValueError
#     print("voer een getal in! ")
#     return getal