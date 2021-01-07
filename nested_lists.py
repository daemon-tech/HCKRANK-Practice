physics_students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    physics_students.append([name, score])
physics_students.sort()
N = len(physics_students)
#removing the lowest grade

grades_list = []

for i in range(N):
    grades_list.append(physics_students[i][1])
grades_list.sort()
min_grade = min(grades_list)
grades_list_temp = gra
