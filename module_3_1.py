# Глобальная переменная для подсчета вызовов функций
calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()  # Увеличиваем счетчик вызовов
    length = len(string)
    upper = string.upper()
    lower = string.lower()
    return (length, upper, lower)

def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счетчик вызовов
    string_lower = string.lower()  # Приводим искомую строку к нижнему регистру
    for item in list_to_search:
        if item.lower() == string_lower:  # Приводим элементы списка к нижнему регистру
            return True
    return False

# Примеры вызовов функций
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches

# Выводим количество вызовов
print(calls)