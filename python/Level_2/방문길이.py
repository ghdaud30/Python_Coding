dirs = "LRLRL"


def solution(dirs):
    answer = 0
    n = 5
    direction = {}
    x = 0
    y = 0
    
    for idx , v in enumerate(dirs):
        dx = x
        dy = y
        
        if(v == 'U'):
            dx -= 1
            if(dx > n or dx < -n):
                dx += 1
            else:
                print(dx,dy)
                if((dx,dy) not in direction):
                    direction[(dx,dy)] = [v]
                    answer += 1
                else:
                    if(v not in direction[(dx,dy)]):
                        direction[(dx,dy)].extend([v])
                        answer += 1
                x = dx         
                       
        elif(v == 'D'):
            dx += 1
            if(dx > n or dx < -n):
                dx -= 1
            else:
                print(dx,dy)
                if((dx,dy) not in direction):
                    direction[(dx,dy)] = [v]
                    answer += 1
                else:
                    if(v not in direction[(dx,dy)] ):
                        direction[(dx,dy)].extend([v])
                        answer += 1
                x = dx
                
        elif(v == 'R'):
            dy += 1
            if(dy > n or dy < -n):
                dy -= 1
            else:
                print(dx,dy)
                if((dx,dy) not in direction):
                    direction[(dx,dy)] = [v]
                    answer += 1
                else:
                    if(v not in direction[(dx,dy)] ):
                        direction[(dx,dy)].extend([v])
                        answer += 1
                y = dy
                
        else:
            dy -= 1
            if(dy > n or dy < -n):
                dy += 1
            else:
                print(dx,dy)
                if((dx,dy) not in direction):
                    direction[(dx,dy)] = [v]
                    answer += 1
                else:
                    if(v not in direction[(dx,dy)] ):
                        direction[(dx,dy)].extend([v])
                        answer += 1
                y = dy
    
    print(direction)
    return answer

print(solution(dirs))