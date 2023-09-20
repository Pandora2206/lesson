"""
Создайте программу, которая определяет, 
является ли введенное слово палиндромом, 
игнорируя пробелы и регистр символов (например, "А роза упала на лапу Азора").
"""

def check_polindrom(string: str)-> bool:
    string =string.replace(" ", '').lower()
    return string == string[::-1]


test_path = "А роза упала на лапу Азора"

print(check_polindrom(test_path))