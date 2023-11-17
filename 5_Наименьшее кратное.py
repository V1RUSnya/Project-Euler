#2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
#Какое самое маленькое число делится нацело на все числа от 1 до 20?
Number = 2
Non_stop = True
while Non_stop:
    count = 1
    for i in range (1,21):
        var = Number % i
        if var == 0:
            count += 1
    if count == 20:
        print(f"Число найдено: {Number}")
        Non_stop = False
    else:
        print(Number)
        Number += 1