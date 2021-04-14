def distribute(list,n):
    max = list[0]  
    min = list[0]  
    for num in set(list): 
        if num>max:
            max=num
        if min>num:
            min=num
    print(min,max)
    distance=(max-min)/n
    list=sorted(list)
    z=[0]*n
    k=0
    i=0
    while k<=n-1 and i<=len(list)-1:
        if min+k*distance<=list[i]<min+(k+1)*distance:
            z[k]=z[k]+1
            i=i+1
        else:
            k=k+1
    z[n-1]=z[n-1]+1
    return z

distribute ([1,2,3,4,5,6,7,8], 2 )
