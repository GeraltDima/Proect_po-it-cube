dengi = int(input("Введите сумму денег на вашей транспортной карте: "))
poezdki = int(input("Введите кол-во ваших поездок: "))
x1_poezdka = 15
ostatok = dengi-poezdki*x1_poezdka
ostatok_text = f"Остаток на проездной карте: {ostatok}₽"
summa = f"Сумма денег на карте: {dengi}"
vozm_proezd = ostatok//x1_poezdka
print(f"\n{summa} \n{ostatok_text}")
print(f"Возможные поездки: {vozm_proezd}\nОстаток на карте после поездок: {ostatok-vozm_proezd}")

