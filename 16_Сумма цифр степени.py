# 2(15) = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.
# Какова сумма цифр числа 2(1000)?

n = 2
for i in range (2,1001):
    n = n * 2
memory = 0
n = str(n)
for i in range (int(len(n))):
    memory = memory + int(n[i])
print(memory) #1366