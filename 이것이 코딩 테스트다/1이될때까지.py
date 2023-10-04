n = 25
k = 3

def 숫자_될때_까지(n,k):
    count = 0
    while(True):
        if(n == 1):
            break

        if(n % k == 0 ):
            n //= k
            count += 1
        else:
            n -= 1
            count += 1

    return(count)

print(숫자_될때_까지(n,k))