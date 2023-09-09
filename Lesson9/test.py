def print_number(n):
    if n == 1:
        return(n)
    else:
        return f"{n} " + f"{print_number(n-1)}"

print(print_number(100))

# 100 + print_number(100-1)
# 100 99 + print_number(99-1)
# 100 99 98 + print_number(98-1)
#
