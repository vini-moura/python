print("Welcome to the rollercoater!")
age= int(input("what's your age?"))
height= int(input("what is you height? (in cm)"))
bill=0

if height >= 120:
    if age <= 7:
        print("Sorry, you have to grow up before you can ride")
        break
    elif age <=12:
        bill +=5
    elif age <=18:
        bill +=7
    elif age >=45 and age<=55:
        bill =0
    else:
        bill +=12

    if input("Do you want a photo? y or n  ") == "y":
        bill +=3

    print(f"your bill is {bill}")
else:
    print("sorry, you have to grow taller before you can ride.")
