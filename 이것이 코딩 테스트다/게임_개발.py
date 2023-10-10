n, m = map(int,input().split())
x,y,direction = map(int,input().split())
d = [[0] * m for _ in range(n)]
d[x][y]= 1

def 게임_개발(n,m,a,b,d):
    info = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    
    def turn_left():
        global direction
        direction -= 1
        if direction == -1:
            direction = 3
            

        


    