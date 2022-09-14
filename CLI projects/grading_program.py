scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

grades={}
for i in scores:
    if scores[i] >= 91:
        grades[i] = 'Outstanding'
    elif scores[i] >= 81:
        grades[i] = 'Exceeds expectations'
    elif scores[i] >= 71:
        grades[i] = 'Acceptable'
    else:
        grades[i] = 'Fail'

print(grades)
