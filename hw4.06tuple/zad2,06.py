n = int(input('Enter number:'))
student_grades = {}
# празен речник
for _ in range(n):
# цикъла се завърта от 0 до n
    student, grade = input('Enter name and grade split by space:').split(' ')
# input взима целият ред ,а split разделя на 2 променливи
    if student_grades.get(student) is None:
# student е ключ .get метода ,който взима стойността на ключа is none проверява дали ключа го има в речника
        student_grades[student] = []
# слагаме на този ключ празен лист,за да добавяме оценки
# ключа е името на ученика ,а стойността са оценките на ученика
    student_grades[student].append(float(grade))
# добавяме оценката към съответният ученик в речника
for student, grades in student_grades.items():
# с този цикъл минаваме през всески ключ(student) и стойност(grades) в речника
    avg = sum(grades)/len(grades)
# пресмятаме средно аритметично
    print(f" {student} -> {grades} (avg: {avg:.2f})")
