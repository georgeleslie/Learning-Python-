import fileinput

studentGrades = {}
total = 0

for line in fileinput.input():
    values = line.strip()
    values = line.split(',')
    
    studentGrades.update({values[0]: int(values[1])})
    
    #print student grades

    for student in studentGrades:
        total = total + studentGrades[student]

average = total / len(studentGrades)

print(f"The average grade is: {average}")