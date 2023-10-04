n = int(input())
#action = input().split()
action = ['R','R','R','U','D','D']

def 상하좌우(n,action):
    move = {'L':-1,'R':1,'U':-1,'D':1}
    plan = [[(i,j) for j in range(1,n+1)] for i in range(1,n+1)]
    x = 1
    y = 1

    for i in range(len(action)):
        if(action[i] == 'L'):
            y += move['L']
            if(y > n or y < 1):
                y -= move['L']
        elif(action[i] == 'R'):
            y += move['R']
            if(y > n or y < 1):
                y -= move['R']
        elif(action[i] == 'U'):
            x += move['U']
            if(x > n or x < 1):
                x -= move['U']
        else:
            x += move['D']
            if(x > n or x < 1):
                x -= move['D']
    
    print(x,y)

상하좌우(n,action)