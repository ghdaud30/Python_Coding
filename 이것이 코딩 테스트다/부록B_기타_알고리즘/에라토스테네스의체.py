import math
n = 1000000

def prime(n):

    prime_list = [True for i in range(n+1)]
    prime = []

    for i in range(2, int(math.sqrt(n)) + 1):
        if(prime_list[i] == True):
            for j in range(2, n // i + 1):
                prime_list[i * j] = False
            # j = 2
            # while(i * j <= n):
            #     prime_list[i * j] = False
            #     j += 1
    
    for i in range(2, n + 1):
        if prime_list[i] == True:
            print(i ,end = ' ')           


print(prime(n))