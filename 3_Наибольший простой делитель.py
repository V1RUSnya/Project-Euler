#Простые делители числа 13195 - это 5, 7, 13 и 29.
#Каков самый большой делитель числа 600851475143, являющийся простым числом?
def main(Number):
    count = 2
    while True:
        WorkNumber = Number % count
        if count == (Number-1):
            return Number
        if WorkNumber == 0:
            Memory = count
            break
        print(WorkNumber, "\t",count)
        count += 1
        
    print(f"{Memory} - найден делитель")
    return Number/Memory


memory = main(600851475143)
backupMemory = 0
while True:
    memory = main(memory)
    if backupMemory == memory:
        print(f"Правильный ответ: {memory}")
        break
    else:
        backupMemory = memory
