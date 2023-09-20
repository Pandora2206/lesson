"""
Напишите программу, которая находит сумму всех чисел от 1 до N, где N вводится пользователем.
""" 

def sum_(n):
    return sum([i for i in range(n+1)])

n = 5 
print(sum_(n))
print(sum([i for i in range(n+1)]))