# Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство

# a2 + b2 = c2
# Например, 32 + 42 = 9 + 16 = 25 = 5.

# Существует только одна тройка Пифагора, для которой a + b + c = 1000.
# Найдите произведение abc.

def check(a,b):
    c = 1000-a-b
    if a**2+b**2==c**2:
        return True
    else:
        return False
    
for a in range (1,1000):
    for b in range (1,1000):
        if check(a,b):
            print(a*b*(1000-a-b))