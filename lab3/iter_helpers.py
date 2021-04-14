import numpy
def transpose(list1):
    list1=numpy.transpose(list1).tolist()
    return(list1)

transpose ([[1 , -1], [2 , 3]])

import itertools
import numpy as np
def scalar_product(list1,list2):
    try:
        list1 =list(map(int,list1))
        list2 =list(map(int,list2))
        func = lambda x,y:x*y
        result_list = list(map(func,list1,list2))
        result=sum(result_list)
        print(result)
    except Valueerror:
        return None
 
 scalar_product([1,'2'],[-1,1])
