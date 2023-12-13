'''
Captcha Generator
#5 characters length
#only alphabets or numeric characters. special characters are not allowed
#atleast 1 Lower case & 1 upper case character. 
#atleast 1 of these trick pairs - {{1, i}, {0, O}, {n, m}, {r, n}, {l, 1}}
'''
import random as rd
import numpy as np

def generate_random_array():
    lst = [-1]*5
    
    # if list is not unique & no element is empty
    while (len(set(lst)) != len(lst)) | (-1 in lst):
        str_pos = rd.randint(0, 4)
        
        x = rd.randint(0, 4) # random number between 0 to 4
        # insert x only if that position is empty & x is not already added
        if (lst[str_pos] == -1) & (x not in lst):
            lst[str_pos] = x
            
    return lst

def captcha():
    s = "     " #captcha str of 5 chars
    
    trick_pair = np.array([['1', 'i'], ['0', 'O'], ['n', 'm'], ['r', 'n'], ['l', '1']])
    lower_char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upper_char = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    num_char = np.arange(0, 10)
    
    # generate an array with 0 - 4 in different slots
    rand_arr = generate_random_array()
    rand_trick = rd.randint(0, 4)
    
    s_list = list(s)
    for i in range (0, 5):
        # 0 - lower, 1 - Upper, 2 - Number, 3 - Trick1, 4 - Trick2
        if (rand_arr[i] == 0):
            s_list[i] = lower_char[rd.randint(0, 25)]
        elif (rand_arr[i] == 1):
            s_list[i] = upper_char[rd.randint(0, 25)]
        elif (rand_arr[i] == 2):
            s_list[i] = str(num_char[rd.randint(0, 9)])
        elif (rand_arr[i] == 3):
            s_list[i] = trick_pair[rand_trick][0]
        elif (rand_arr[i] == 4):
            s_list[i] = trick_pair[rand_trick][1]
        else:
            print(i, ": unknown captcha type")
    s = "".join(s_list)
    return s


#main program
print(captcha())
