import numpy as np

def game_v3(num):
    
    num_lst = list(range(1,101))
    count = 0
    
    while len(num_lst) >= 4:
        mid_lst = int(len(num_lst)/2 - 1)
        count += 1
        
        if num >= num_lst[mid_lst]:
            num_lst = list(filter(lambda x: True if x >= num_lst[mid_lst] else False, num_lst))
            print(num_lst)  
        if num <= num_lst[mid_lst]:
            num_lst = list(filter(lambda x: True if x <= num_lst[mid_lst] else False, num_lst))
            print(num_lst)
        
        if len(num_lst) == 3:
            if num != num_lst[0] and num != num_lst[1]:
                print(num_lst[2])
                print(count)
            elif num != num_lst[0] and num != num_lst[2]:
                print(num_lst[1])
                print(count)
            elif num != num_lst[1] and num != num_lst[2]:
                print(num_lst[0])
                print(count)
        elif len(num_lst) == 2:
            if num == num_lst[0]:
                print(num_lst[0])
                print(count)
            else:
                print(num_lst[1])
                print(count)

          
game_v3(33)   
