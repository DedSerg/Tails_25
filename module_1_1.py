# 1st program
result = 9 ** 0.5 * 5
print(result)

# 2nd program
result = (9.99 > 9.98) and (1000 != 1000.1)
print(result)

# 3rd program
result1 = 2 * 2 + 2  # без приоритета
result2 = 2 * (2 + 2)  # с приоритетом для сложения
print(result1)
print(result2)
comparison = result1 == result2
print(comparison)

# 4th program
number_str = '123.456'
number_float = float(number_str)  # Преобразуем строку в дробное число
shifted_number = number_float * 10  # Умножаем на 10, чтобы сместить 4
first_digit_after_decimal = int(shifted_number) % 10  # Получаем первую цифру после запятой
print(first_digit_after_decimal)