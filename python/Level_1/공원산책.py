park = ["OSO","OOO","OXO","OOO"]
routes = ["E 2","S 3","W 1"]


def solution(park, routes):
    answer = []
    obstacle = []

    for idx ,row in enumerate(park):
        for idy ,col in enumerate(row):
            if(col == 'S'):
                x = idx
                y = idy
            if(col == 'X'):
                obstacle.append((idx,idy))

    print(obstacle)
    dx = x
    dy = y
    for i in routes:
        direction = i[0]
        distance = int(i[-1])

        if(direction == "N" ):
            for j in range(1,distance+1):    
                dx -= 1
                if(dx >= len(park) or dx < 0 or (dx,y) in obstacle):
                    dx = x 
                    break

        elif(direction == 'S'):
            for j in range(1,distance+1):
                dx += 1
                if(dx >= len(park) or dx < 0 or (dx,y) in obstacle):
                    dx = x
                    break
        elif(direction == 'W'):
            for j in range(1,distance+1):
                dy -= 1
                if(dy >= len(park[0]) or dy < 0 or (x,dy) in obstacle):
                    dy = y
                    break
        else:
            for j in range(distance):
                dy += 1
                if(dy >= len(park[0]) or dy < 0 or (x,dy) in obstacle):
                    dy = y
                    break
        x = dx
        y = dy       

    answer.append(x)
    answer.append(y)
        
    return answer

print(solution(park, routes))
