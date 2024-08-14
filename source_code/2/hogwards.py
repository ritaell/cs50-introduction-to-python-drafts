'''
students = ["Harry" , "Hermione" , "Ron"]

for student in students:
    print(student)

for i in range(len(students)):
    print(i+1 , students[i])
    '''

#--------------------------
'''
students={
    "Hermione" : "Gryfyndor",
    "Harry" : "Gryfyndor",
    "Ron" : "Gryfyndor",
    "Draco" : "Slytherin"
}

for student in students:
    print(student , students[student])
    '''
#--------------------------------------
students=[
    {"name" : "Hermiony" , "house" : "Gryfyndor" , "patronus" : "otter"},
    {"name" : "Harry" , "house" : "Gryfyndor" , "patronus" : "stag"},
    {"name" : "Draco" , "house" : "Slytherin" , "patronus" : None}
]

for student in students:
    print(student["name"])

