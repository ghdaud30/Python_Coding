import string
n = input()

def 왕실의나이트(n):
    m = 8
    x = int(n[1])
    y = int(ord(n[0])) - int(ord('a')) +1
    dx = [2, 2, 1, 1, -2, -2, -1 , -1]
    dy = [1, -1, 2, -2, 1 , -1 , 2 , -2]
    count = 0 
    
    for i in range(len(dx)):
        x += dx[i]
        y += dy[i]

        if(x < 1 or x > m or y < 1 or y > m):
            x -= dx[i]
            y -= dy[i]
            continue
        
        count += 1
        x = int(n[1])
        y = int(ord(n[0])) - int(ord('a')) +1

    return(count)


print(왕실의나이트(n))