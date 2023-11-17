#Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. 
#Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

#Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
#999 999
def reverse(num):
    num = str(num)
    num = num[::-1]
    return int(num)

first = 900
second = 900
memory = 0
for first in range (900,999):
    for second in range (900,999):
        result = first*second
        if result == reverse(result) and result > memory:
            memory = result
            print(f"Найдено новое число палиндром. {memory}\nРезультат умножения {first} и {second}")