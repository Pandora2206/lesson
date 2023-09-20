def get_task(n: int, k:int, colors: str) -> list[list[int]]:
    
    # офицеры - офицеры, ваше сердце под прицелом ... 
    list_index = {i+1: color for i, color in enumerate(colors) }
    count_w = colors.count('w')

    vzvods = []
    index_w = [i for i in list(list_index.keys()) if list_index[i]=="w"]

    while len(vzvods) < n//k+1:
            # шаг вправо (беру всех)
        index_ = index_w[0]    
        vzvod = []
        count = 0
        for i in range(index_, index_ +k):
            if list_index[i] =="v" and len(vzvod)<k:
                vzvod.append(i)
            else:
                break
        # шаг влево  
        for i in reversed(list_index):
            if len(vzvod)<k and list_index[i] =="v":
                vzvod.append(i)
            else:
                break
            

        if len(vzvod)<k and :
            # шаг вправо (беру всех)
            index_ = index_w[-1]
            vzvod = []
            count = 0
            last_index = list(list_index.keys())[-1]
            for i in range(index_+1 , last_index+1):
                if list_index[i] =="v" and len(vzvod)<k:
                    vzvod.append(i)
                else:
                    break
            # шаг влево  
            for i in reversed(list(list_index.keys())[:index_-1]):
                if len(vzvod)<k and list_index[i] =="v":
                    vzvod.append(i)
                else:
                    break

        if len(vzvod)==k:            
            vzvod.append(index_)
            index_w.remove(index_)
            for item in vzvod:
                list_index.pop(item)

            vzvods.append(vzvod)

 

test = [12, 2, "wwvwvvvvvvwv" ]
get_task(*test)