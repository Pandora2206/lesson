# list1 = [] # 20 elem
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 10, 9 ,8 , 7, 6,5 , 4, 3, 2, 1

import random

list1 = []
r = lambda: random.randint(-100, 100)
for i in range(20):
    list1.append(r())  # заполнил рандомными числами
print(list1)


def get_max(list_input: list) -> int:
    """

    :param list_input: Входной список integer
    :return: максимальный элемент
    """
    max_elem = list_input[0]
    for elem in list_input:
        if max_elem < elem:
            max_elem = elem

    return max_elem


max_elem = get_max(list1)

print('MAX: ', max_elem)
