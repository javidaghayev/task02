# task1 

height = float(input("Boyunuz: "))
weight = float(input("Chekiniz: "))

bmi = round(weight / (height / 100)**2, 2)


if bmi <= 18.5:
    print("Zeif")
elif bmi <= 24.9 and bmi > 18.5:
    print("Normal")
elif bmi <= 29.9 and bmi > 24.9:
    print("Kilolu")
else:
    print("Obezite")
print(bmi)




# task2 


product = input("Mehsulu daxil edin: ")
price = int(input("Qiymeti daxil edin: "))
tax = (price * 18) / 100
total_price = price + tax

if total_price >= 50 and total_price < 100:
    print("10 AZN kupon qazandiniz ")
elif total_price >= 100:
    print("15 AZN kupon qazandiniz")
else:
    print("Kupon qazanmaq ucun minimum 50 azn (edv daxil) alis-veris edin")


# task3 

choice1 = int(input("Neqliyyat vasitesi secin: (1) Avtomobil, (2) Yuk masini, (3) Avtobus  "))
choice2 = int(input("Mesafeni qeyd edin: "))

if choice1 == 1:
    print("Qiymet: ", choice2 * 0.50, "$")
elif choice1 == 2:
    print("Qiymet: ", choice2 * 1, "$")
elif choice1 == 3:
    print("Qiymet: ", choice2 * 2, "$")
else:
    print("Yanlish secim ! ")