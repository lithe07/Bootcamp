oppervlakte = int(input('Hoeveel m2 vloerbedekking heeft u nodig?'))
prijs_m2 = 40

if oppervlakte >= 150:
    prijs_m2 = 35
elif oppervlakte >= 80:
    prijs_m2 = 38

totaal = prijs_m2 * oppervlakte

print(f'Het totaalbedrag is voor een oppervlakte van {oppervlakte} m2 is: Eur ' + str(totaal))
