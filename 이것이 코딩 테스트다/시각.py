n = int(input())

def 시각(n):
    count = 0
    num_list = []

    for number in range(61): 
        if '3' in str(number):  
            num_list.append(int(number))
    print(num_list)

    for i in range(n+1):
        for j in range(60):
            for k in range(60):
                if(i in num_list or j in num_list or k in num_list):
                    count += 1
    
    print(count)

시각(n)
