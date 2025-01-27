# Переменные
homework_completed = 12  # Количество выполненных ДЗ
hours_spent = 1.5        # Количество затраченных часов
course_name = 'Python'    # Название курса

# Вычисляем среднее время на одно задание
time_per_assignment = hours_spent / homework_completed

# Выводим на экран требуемую строку
print(f"Курс: {course_name}, всего задач: {homework_completed}, затрачено часов: {hours_spent}, среднее время выполнения {time_per_assignment:.3f} часа.")