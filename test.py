from Tasks.Task__11.Product import *

p = Product("Test", 100, 10)
p.display_info()

value = setattr(p, "name")
print(value)