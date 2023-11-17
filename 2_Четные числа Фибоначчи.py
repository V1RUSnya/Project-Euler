#Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:

#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

#Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.

past,present,memory,memorycount = 1,2,0,0
print(f"{past}\n{present}\n")
while True:
    temp = past + present
    past = present
    present = temp
    if present % 2 != True:
        if present <= 4000000:
            print(f"{present}\n")
            memory = memory + present
            memorycount += 1
        else:
            break
print(f"\nСумма всех чисел: {memory}\nВсего четных чисел: {memorycount}\n")