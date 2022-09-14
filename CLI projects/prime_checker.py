n = int(input("Inser a number to check "))

def prime_cheker(n):
    a = True
    for i in range(2, n):
        if n % i == 0:
            a = False
    if a:
        print('Its a prime number')
    else:
        print('Its not a prime number')

prime_cheker(n)
