from collections import deque

maps = [[1,0,1,1,1],
        [1,0,1,0,1],
        [1,0,1,1,1],
        [1,1,1,0,1],
        [0,0,0,0,1]]

def solution(maps):
    answer = 0
    x = 0
    y = 0
    n = len(maps)
    m = len(maps[0])
    moves = [(0,1),(0,-1),(1,0),(-1,0)] 
    visited = [[False for _ in range(m)] for _ in range(n)]
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    
    while(queue):
        x,y = queue.popleft()

        for move in moves:
            dx = move[0]
            dy = move[1]
            if(x + dx >= n or x + dx < 0 or y + dy >= m or y + dy < 0):
                continue
            if(maps[x+dx][y+dy] == 0):
                continue
            else:
                if(maps[x+dx][y+dy] == 1 and visited[x+dx][y+dy] == False):
                    
                    maps[x+dx][y+dy] += maps[x][y]
                    x += dx
                    y += dy
                    visited[x][y] = True
                    queue.append((x,y))
    
    print(maps)
    
    if(maps[n-1][m-1] == 1):
        return -1
    else:
        return maps[n-1][m-1]
           
         
print(solution(maps))