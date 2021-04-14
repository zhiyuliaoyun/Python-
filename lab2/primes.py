def get_primes(n):
    result=[]
    for i in range(2,n+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            result=result+[i]
    return result

get_primes(11)
