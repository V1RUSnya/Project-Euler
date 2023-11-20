#Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-е простое число - 13.
#Какое число является 10001-м простым числом?
num = 2
numbersCount = 0
while True:
    num +=1
    count = 0
    for i in range (num+1):
        if i != 0:
            if num%i == 0:
                count += 1
                if count >= 3:
                     break
    if count == 2:
            print(f"Найдено число {num}! Осталось найти {10001-numbersCount}")
            numbersCount +=1                
    if numbersCount == 10001:
        break            
print(f"10001 число: {num}")
