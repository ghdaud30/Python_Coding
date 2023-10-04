wallpaper = ["..", "#."]

def Clean_up_your_desktop(wallpaper):
    answer = []
    coordinate = []

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if(wallpaper[i][j] == '#'):
                coordinate.append((i,j))
                coordinate.append((i+1,j+1))

    min_x = 50
    min_y = 50
    max_x = 0
    max_y = 0
    for k in range(len(coordinate)):
        for t in range(len(coordinate[k])):
            if t == 0:
                x = coordinate[k][t]
                if( min_x >= x):
                    min_x = x
            else:
                y = coordinate[k][t]
                if( min_y >= y):
                    min_y = y

    for k in range(len(coordinate)):
        for t in range(len(coordinate[k])):
            if t == 0:
                x = coordinate[k][t]
                if( x >= max_x):
                    max_x = x
            else:
                y = coordinate[k][t]
                if( y >= max_y):
                    max_y = y
    
    
    print(min_x)
    print(min_y)
    print(max_x)
    print(max_y)
    answer.append(min_x)
    answer.append(min_y)
    answer.append(max_x)
    answer.append(max_y)

    return answer

print(Clean_up_your_desktop(wallpaper))