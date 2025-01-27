# Данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Иоанн', 'Матфей', 'Лука', 'Пётр', 'Марк'}

# Преобразуем множество студентов в упорядоченный список
students_list = sorted(students)

# Создаем словарь для хранения средних баллов
average_grades = {}

# Подсчитываем средний балл для каждого ученика
for i in range(len(students_list)):
    student = students_list[i]
    student_grades = grades[i]
    average_grade = sum(student_grades) / len(student_grades)
    average_grades[student] = average_grade

print(average_grades)

# Выводим результат
print("Средние баллы учеников:")
for student, avg in average_grades.items():
    print(f"{student}: {avg:.2f}")