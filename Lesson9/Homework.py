list_1=[1,[2,[3,[4,["",[]]]]]]

def get_list(stop: int, list_result: list = []) -> list:
    
    if stop == 0:
        return list_result
    else:
        
        return get_list(stop-1, list_result[0])



print(get_list(5))
#  1. 5, []
#  2. 5, [4, []]
#  3. 5, [4, [3, []]]