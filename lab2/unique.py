def compress(list):
    a=[]
    for i in set(list):
        count = list.count(i)
        a=a+[(i,count)]
    return a

compress([1 , 2 , 1 , 3])
