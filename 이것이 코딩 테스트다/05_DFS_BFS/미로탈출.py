from collections import deque
n = 5
m = 6
maze = [[1,0,1,0,1,0],
        [1,1,1,1,1,1],
        [0,0,0,0,0,1],
        [1,1,1,1,1,1],
        [1,1,1,1,1,1]]

def solution(n,m,maze):
    move = [(1,0),(-1,0),(0,-1),(0,1)]    
    x = 0
    y = 0
    queue = deque()
    queue.append((x,y))

    while(queue):
        x , y = queue.popleft()
        
        for dx,dy in move:
            nx = x + dx
            ny = y + dy
            if(nx >= n or nx < 0 or ny >= m or ny < 0 
                or maze[nx][ny] == 0 ):
                continue
            if(maze[nx][ny] == 1):
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx,ny))
    print(maze)

    return maze[n-1][m-1]

print(solution(n,m,maze))

            