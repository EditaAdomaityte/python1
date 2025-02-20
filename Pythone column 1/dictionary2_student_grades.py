student_grades={}

def add_student(student, grade):
    student_grades[student]=grade
    print(f"Student '{student}' added with grade '{grade}'.")

def remove_student(student):
    if student in student_grades:
        del student_grades[student]
        print(f"Student '{student}' removed")

def display_students():
    print("Student and their grades")
    for student, grade in student_grades.items():
        print(f"{student}:{grade}")

#Function to upgrade the grade
def update_grade(student, grade):
    if student in student_grades:
        student_grades[student]=grade
        print (f"Student '{student}' grade was updated and is '{grade}'.")
    else:
        print(f"Student '{student}' was not found")

def find_grade(student):
    if student in student_grades:
        print(f"{student}'s grade is {student_grades[student]}")# using [student]- because it is a key
    else:
        print(f"Student {student} is not found.")

def average_grade():
    if len(student_grades)>0:
        total=sum(student_grades.values())
        number_students=len(student_grades)
        avg=total/number_students
        print(f"The average grade of all students is {avg:.2f}.")#gives 2 #after .
    else:
        print("No students in gradebook.")

add_student("JoAnna",10)
add_student("Nate",9)
add_student("Sabra",8)
add_student("Edita",8)
add_student("John",8)
add_student("Lindsay",8)

remove_student("Nate")

display_students()

update_grade("Sabra",10)
update_grade("Nate",9)
display_students()
find_grade("Sabra")

average_grade()
