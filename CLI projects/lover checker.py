# -*- coding: utf-8 -*
print("Wellcome to the Love Calculator")
name1 = input("What is your name? ")
name2 = input("What is his/her name?")
name1 = name1.lower()
name2 = name2.lower()

t = name1.count("t")
r = name1.count("r")
u = name1.count("u")
e = name1.count("e")
l = name1.count("l")
o = name1.count("o")
v = name1.count("v")
e = name1.count("e")

dezena = t+r+u+e
unidade = l+o+v+e

t = name2.count("t")
r = name2.count("r")
u = name2.count("u")
e = name2.count("e")
l = name2.count("l")
o = name2.count("o")
v = name2.count("v")
e = name2.count("e")

dez = dezena+t+r+u+e
uni = unidade+l+o+v+e
total = str(dez) + str(uni)
total = int(total)

if total < 10 and total>90:
    print(f"your score is {total}, and you go together like coke and mentos")
elif total>=40 and total<=50:
    print(f"your score is {total}, and you are alright together")
else:
    print(f"your score is {total}")
