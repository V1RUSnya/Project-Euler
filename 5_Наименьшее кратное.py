#2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
#Какое самое маленькое число делится нацело на все числа от 1 до 20?
from math import gcd
num = 1
for i in range(2, 21):
    num = (num * i) // gcd(num, i)
    print(num)
print(f"{num} - наименьшее число")
