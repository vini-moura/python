import random

number = random.randint(1,100)
y=0

print('Estou pensando número entre 1 e 100.\nQual é?')
while y != number :
    y = int(input())
    if y<number:
        print("\nNão, é um número maior")
    else:
        print("\nNão, é um número menor")
else:
    print("\nÉ esse número. Parabéns.")
