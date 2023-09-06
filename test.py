def list_sort(list_input):
    list_abs = [abs(i) for i in list_input]
    print(list_abs)
    checker = False
    for i in range(len(list_input)-1):
        for j in range(len(list_input)-2):
            if abs(list_input[j])>abs(list_input[j+1]):
                checker = True  
                list_input[j], list_input[j+1] = list_input[j+1], list_input[j]
        if not checker:
            return

list = [1,2,3,-1,-2,-3]
list_sort(list)

print(list)