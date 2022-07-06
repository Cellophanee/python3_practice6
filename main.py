class Student:
    students = dict()
    n = int(input("Введіть кількість студентів:"))
    for i in range(n):
            sname = input("Введіть ім'я студента:")
            marks= []
            for j in range(3):
                mark = int(input("Введіть оцінку:"))
                marks.append(mark)
            students[sname] = marks
    print(students)
    for i in range(len(students)):
        b = sum(marks) / 3
        print(sname, ' - ', b)