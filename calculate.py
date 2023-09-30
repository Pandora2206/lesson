

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
