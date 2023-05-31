data=[['Rachel', -50],
           ['Mawer', -50],
           ['Sheen', -50],
           ['Shaheen', 51]]

students=[]

def find_second_lowest(students):
    # Find the second lowest grade
    grades = [student[1] for student in students]
    unique_grades = sorted(set(grades))

    if len(unique_grades) < 2:
        return []  # Not enough unique grades

    second_lowest_grade = unique_grades[1]

    # Find students with the second lowest grade
    second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]

    return second_lowest_students


for _ in range(0,4):
    name =data[_][0]
    score = data[_][1]
    students=students+[[name,score]]



second_lowest_students = find_second_lowest(students)

if second_lowest_students:
    for student in second_lowest_students:
        print(student) 



