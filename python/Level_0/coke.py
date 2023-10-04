
def examine_coke(a, b, n):
    sum = 0
    while n >= a:
        
        sum += int((n / a)) * b  # 6  8  9
        c = n % a   #  2  2  1
        n = int((n / a)) + c  #  8  4  2

    if(n <= a):
        return sum
    
a = 2
b = 1
n = 20

sum = examine_coke(a,b,n)
print(sum)



