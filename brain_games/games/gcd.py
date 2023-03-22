from random import randint 
import prompt 
from math import gcd

general_question = 'Find the greatest common divisor of given numbers.'

def play():
    f_num = randint(0, 100)
    s_num = randint(0, 100)
    two_nums = f'{f_num} {s_num}'
    result = gcd(f_num, s_num)
    
    return two_nums, str(result) 


