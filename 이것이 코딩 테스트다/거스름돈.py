money = 1570

def 거스름돈(money):
    coin = [500,100,50,10]
    count = 0

    for i in coin:
        count += (money // i)
        money %= i
    
    return count

print(거스름돈(money))