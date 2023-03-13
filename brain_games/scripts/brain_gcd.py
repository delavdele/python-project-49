#!/usr/bin/env python3
from random import randint 
import prompt 
from math import gcd

def gcd():
    f_num = randint(0, 100)
    s_num = randint(0, 100)
    two_nums = f'{f_num} {s_num}'
    result = math.gcd(f_num, s_num)
    
    return two_nums, result 



if __name__ == '__main__':
    main()
