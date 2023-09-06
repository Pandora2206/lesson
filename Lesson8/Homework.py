"""
1. Строки надо считать +
2. Определить длину каждой строки +
3. Найти наибольшую строку +
4. Добавить * к меньшим строкам 
5. Вывод новых строк 
"""

# strings = ['привет', 'пока', 'лол']
# aling_string_list = ['привет', '**пока', '***лол']
def aling_string(strings: list[str]) -> list[str]:
    aling_string_list = []
    max_len = len(strings[0])
    for string in strings:
        if len(string) < max_len:
            new_string = (max_len - len(string))*"*"+string
            aling_string_list.append(new_string)
        else:
            aling_string_list.append(string)

    return aling_string_list


string_list = []
n = int(input("Введите кол-во строк: "))
for _ in range(n):
    new_str = input("Введите строку: ")
    string_list.append(new_str)

string_list_sort = sorted(string_list, key= lambda a: len(a), reverse=True)
aling_strings = aling_string(string_list_sort)

# len(str) - возвращает длину строки 
print(string_list_sort)
print(aling_strings)
