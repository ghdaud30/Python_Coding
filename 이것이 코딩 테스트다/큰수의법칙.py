n = 5
m = 8
k = 3
t = [2,4,5,4,6]


def 큰수의법칙(n,m,k,t):
    sum = 0
    t = sorted(t,reverse=True)
    max_t = t[0]
    max2_t = t[1]
    k1 = 0
    
    for i in range(m):
        if(k1 < k):
            sum += max_t
            k1 += 1
        else:
            sum += max2_t
            k1 = 0
    
    return sum

print(큰수의법칙(n,m,k,t))