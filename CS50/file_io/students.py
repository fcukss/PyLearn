# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")


students=[]
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {'name': name, 'house': house}
        students.append(student)

# def get_name(student):
#     return student["name"]
#
# for student in sorted(students,key=get_name):
#     print(f"{student['name']} is in {student['house']}")

#the same with using lambda
for student in sorted(students,key=lambda student: student['name']):
    print(f"{student['name']} is in {student['house']}")