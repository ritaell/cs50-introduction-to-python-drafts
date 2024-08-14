import csv
'''
students=[]
with open("grades.csv") as data:
    for line in data:
        row=line.rstrip().split(",")
        student={"name":row[0], "grade":row[1]}
        students.append(student)

for student in sorted(students,key=lambda student: student["name"]):
    print(f"{student['name']}'s grade is {student['grade']}")
'''

students=[]
with open("grades.csv") as data:
    reader=csv.DictReader(data)
    for row in reader:
        students.append({"name": row["name"],"grade": row["grade"]})


for student in sorted(students,key=lambda student: student["name"]):
    print(f"{student['name']}'s grade is {student['grade']}")
