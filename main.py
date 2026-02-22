print("Liczby podzielne przez 5:")

podzielne = []

for liczba in range(0, 101):
    if liczba % 5 == 0:
        podzielne.append(liczba)
print(podzielne)
#teraz podnosze te liczby do potegi 3

print("Liczby w potędze trzeciej:")

szesciany = []

for liczba in podzielne:
    wynik = liczba ** 3
    szesciany.append(wynik)

print(szesciany)