# Записываем строку в переменную example
example = "Cинхрофазотрон"

# Выводим первый символ строки
print("Первый символ:", example[0])

# Выводим последний символ строки, используя отрицательный индекс
print("Последний символ:", example[-1])

# Выводим вторую половину строки
length = len(example)
if length % 2 == 0:
    second_half = example[length // 2:]  # Если четное, берем вторую половину
else:
    second_half = example[length // 2 + 1:]  # Если нечетное, пропускаем середину
print("Вторая половина строки:", second_half)

# Выводим строку наоборот
reversed_example = example[::-1]
print("Слово наоборот:", reversed_example)

# Выводим каждый второй символ строки
every_second_char = example[::2]
print("Каждый второй символ:", every_second_char)