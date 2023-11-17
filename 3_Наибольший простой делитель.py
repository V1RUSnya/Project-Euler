#Простые делители числа 13195 - это 5, 7, 13 и 29.
#Каков самый большой делитель числа 600851475143, являющийся простым числом?
from numba import njit #Движок для ускорения

def test():
    for i in range (1,13195):
        a = 13195 % i
        if a == 0:
            memory = i
            print(f"{i} - подходит")
    print(f"{memory} - наибольший делитель") #Пример

@njit
def main():
    count = 1
    while True:
        Number = 600851475143 % count
        if Number == 0:
            Memory = count
        print(f"{Memory} - Последний наибольший делитель!\t\t{count}")
        count += 1
        if count == 600851475142:
            break
    print(f"{Memory} - наибольший делитель (Кроме самого числа)")

main()