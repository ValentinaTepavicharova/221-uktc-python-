def class_room(**kwargs):
    result=''
    for student_name, grades in kwargs.items():
        result+= student_name+'\n'
        for grade in grades:
            result+=str(grade)+'\n'
    return result

print(
class_room(
Спиридон=[2, 3, 3, 4, 6],
Стамат=[6, 6, 6, 2],
Анджелина=[3, 3, 4, 3, 5]
)
)