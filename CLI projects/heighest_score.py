scores = input("Input a list of students' grades separated by space\n").split()

for n in range(0, len(scores)):
    scores[n] = int(scores[n])
print(scores)

heighest=0
for x in scores:
    if(x > heighest):
        heighest = x
print(f"the heighest score is {heighest}")
