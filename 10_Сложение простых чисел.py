# Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
# Найдите сумму всех простых чисел меньше двух миллионов.
a,memory=1,0
while a<=2000000:
    a += 1
    count = 0
    for i in range (1,int(a**0.5+1)):
        if a%i==0:
            count += 1
            if count >= 2:
                break
    if count == 1:
        print(a)
        memory += a
print(memory)