from collections import deque

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]	

def solution(maps):
    answer = 0
    x = 0
    y = 0
    n = len(maps)
    m = len(maps[0])
    moves = [(0,1),(0,-1),(1,0),(-1,0)] 
    visited = [[False]*m for _ in range(n)]
    queue = deque()
    queue.append((x,y))
    #처음 좌표를 큐에 넣고 나서 방문 처리를 해줍니다
    visited[x][y] = True
    
    while(queue):
        # BFS를 이용해서 주변을 돌고 난 후에 pop을 해줍니다
        x,y = queue.popleft()

        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            if(nx >= n or nx < 0 or ny >= m or ny < 0 or maps[nx][ny] == 0):
                pass
            else:     
                if(not visited[nx][ny]):
                    maps[nx][ny] += maps[x][y]
                    visited[nx][ny] = True
                    queue.append((nx,ny))
    
    print(maps)
    
    if(maps[n-1][m-1] == 1):
        return -1
    else:
        return maps[n-1][m-1]
           
         
print(solution(maps))