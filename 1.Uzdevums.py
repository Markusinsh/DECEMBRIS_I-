#lai lietotajs ieraksta skaitli (piemeram 12)
ievaditais_skaitlis = int("12")

#Cikls kad skaitaw
summa = 0
for skaitlis in range(1, ievaditais_skaitlis + 1):
    summa += skaitlis

#parada gala rezultatu
print(f"Skaitļu no 1 līdz {ievaditais_skaitlis} summa ir {summa}")
