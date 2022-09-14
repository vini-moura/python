import numbers
import random

nletters = int(input("How many letters do you wish?\n"))
nnumbers = int(input(f"How many numbers do you wish?\n"))
nsymbols = int(input(f"How many symbols do you wish?\n"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', ';', '+']

# for i in range(0,qntd):

passw = []
for i in range(0, nletters):
    passw += random.choice(letters)
for i in range(0, nnumbers):
    passw += random.choice(numbers)
for i in range(0, nsymbols):
    passw += random.choice(symbols)

random.shuffle(passw)

password = ''
for i in passw:
  password += i
print(password)
