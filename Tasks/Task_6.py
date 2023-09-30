"""Напишите программу, которая переводит числа из 2 сс в 10 сс"""
import math
a = 101110111
sum_elements = 0
for i, item in enumerate(reversed(str(a))):
    item = int(item)
    sum_elements+=item*(2**i)


sum_elements_2 = sum([int(item)*(2**i) for i, item in enumerate(reversed(str(a)))])
print(sum_elements)
print(sum_elements_2)