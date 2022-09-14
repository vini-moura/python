student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

soma = 0
for i in student_heights:
    soma += i
print(soma)

divisor = 0
for i in student_heights:
    divisor += 1
print(divisor)
media = soma / divisor
print(f'The medium height is: {media}')

##########

student_scores = input("Input a list of students score ").split()
for n in range(0,len(student_scores)):
    student_scores[n]= int(student_scores[n])

n = 0
for i in student_scores:
    if(i >= n):
        n = i

print(f'the highest score is: {n}')







