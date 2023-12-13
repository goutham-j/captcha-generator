import random

def generate_random_array():
    lst = [-1]*5
    
    while (len(set(lst)) != len(lst)) | (-1 in lst):
        str_pos = random.randint(0, 4)
        
        x = random.randint(0, 4)
        if (lst[str_pos] == -1) & (x not in lst):
            lst[str_pos] = x
            
    return lst 

rand_arr = generate_random_array()
print(rand_arr)
