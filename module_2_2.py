# Ввод трех целых чисел
first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))

# Условная конструкция для определения количества одинаковых чисел
if first == second == third:
    print(3)  # Все числа равны
elif first == second or first == third or second == third:
    print(2)  # Хотя бы два числа равны
else:
    print(0)  # Все числа разные