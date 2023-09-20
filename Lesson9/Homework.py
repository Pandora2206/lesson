list_1=[1,[2,[3,[4,["",[]]]]]]

def get_list(stop: int, list_result=None) -> list:
    
    if list_result is None:
        list_result = []
    if stop == 0:
        return list_result
    else:
        
        return get_list(stop-1, list_result)



print(get_list(0))
#  1. 5, []
#  2. 5, [4, []]
#  3. 5, [4, [3, []]]