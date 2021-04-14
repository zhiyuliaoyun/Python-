def merge(list1,list2): 
    list= list1+list2
    for m in range(len(list)-1):
        for n in range(m+1, len(list)):
            if list[m]> list[n]:
                temp = list[n]
                list[n] = list[m]
                list[m] = temp
    print(list)
