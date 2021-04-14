def calculate_special_sum(n):
    sum=0
    part=0
    for i in range (1,n):
        part=i*i*(i+1)
        sum=sum+part
    print(sum)
    
calculate_special_sum(3)
