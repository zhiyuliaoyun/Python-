def get_nearest_lucky_ticket(x):
    x1 = x2 = int(x)
    sum1 = 0
    sum2 = 1
    sum3 = 0
    sum4 = 1
    while sum1!=sum2:
        st=str(x1)
        st1=[st[i] for i in range (1,len(st),2)]
        st2=[st[i] for i in range (0,len(st),2)]
        sum1=0
        sum2=0
        print(st1)
        for i in range (0,len(st1)):    
            a = int(st1[i])
            sum1 = sum1 + a
        for i in range (0,len(st2)):
            b = int(st2[i])
            sum2 = sum2 + b
        x1 = int(x1) + 1
    x1 = x1 - 1
    while sum3!=sum4:
        st=str(x2)
        st1=[st[i] for i in range (1,len(st),2)]
        st2=[st[i] for i in range (0,len(st),2)]
        sum3=0
        sum4=0
        for i in range (0,len(st1)):    
            a = int(st1[i])
            sum3 = sum3 + a
        for i in range (0,len(st2)):
            b = int(st2[i])
            sum4 = sum4 + b
        x2 = x2 - 1
    x2 = x2 + 1
    distance1= int(x1)-int(x)
    distance2= int(x)-int(x2)
    if distance1==distance2:
        print(x1,x2)
    if distance1<distance2:
        print(x1)
    if distance1>distance2:
        print(x2)

get_nearest_lucky_ticket(578898)
