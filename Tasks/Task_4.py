"""
Создайте список чисел и напишите программу, которая находит наименьшее и наибольшее число в списке.
"""

import random 

list_items = [random.randint(-100, 100) for _ in range(10)]
print(list_items)


def get_result(list_items):
    min_ = min(list_items)
    max_ = max(list_items)
    index_min = 0
    index_max = 0 
    for i, item in enumerate(list_items):
        
        if item == min_:
            index_min = i
        if item == max_:
            index_max = i

    print(min_)
    print(max_)
    print(index_min)
    print(index_max)

get_result(list_items)



