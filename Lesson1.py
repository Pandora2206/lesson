# int a = 0;
# str a = "0";

# type - тип переменной
# a = 0.0
# print(type(a))
# типы данных
# int - тип целочисленный
a_int = 10
print(type(a_int))

# float - дробные значения
a_float = 10.0
# 0.1111 = .1111
print(type(a_float))

# string - строки
# char - символ '1', 'g', ','
a_str = '10.10'
print(type(a_str))

# boolean - bool - логический тип данных
a_bool = True
# True = 1
# False = 0
# if a_bool == 1:
#     print(True)
# a_bool = False
print(type(a_bool))

# Жесткая типизация
a_new_int = int(a_float)
print(a_new_int, type(a_new_int))

a_new_float = float(a_str)
print(a_new_float, type(a_new_float))

a_new_int = round(a_new_float, 0)
print(a_new_int, type(a_new_int))

# Операции с тип данных

a = 10
b = 5
# 10/2 = 5.000000000000000000000000000003
print(a + b)  # Сложение
print(a - b)  # вычитание
print(a * b)  # Умножение
print(a / b)  # Деление
print(a // b)  # Целая часть от деления
print(a % b)  # Остаток от деления
print(a ** b)  # Возведение в степень
print(a ** (1 / b))

# Логические операторы
a = 10
b = 10
# Возвращают BOOLEAN
print(a > b)  # больше
print(a >= b)  # больше или равно
print(a < b)  # меньше
print(a <= b)  # меньше или равно
print(a == b)  # равенство
print(a != b)  # неравенство

# Условные операторы

if a == b:
    print(True)
else:
    print(False)

if a is b:
    print(True)
else:
    print(False)

# Операторы проверки

try:
    a = 10 / 1
except ZeroDivisionError:
    a = 0
finally:
    print(a)
