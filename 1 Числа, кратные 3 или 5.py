#Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
#Найдите сумму всех чисел меньше 1000, кратных 3 или 5.

def findnum():
    while True:
        a = input()
        a = int(a) % 2
        if a == True:
            print("Нечетное") #Пример поиска числа

memory = 0
countmemory = 0
for i in range (0,1000):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
        memory = memory + i
        countmemory += 1
print(f"Сумма нечетных чисел в радиусе от 1 до 1000: --{memory}\nВсего чисел: --{countmemory}")
