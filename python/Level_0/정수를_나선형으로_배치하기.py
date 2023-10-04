n = 1000


def 정수를_나선형으로_배치하기(n):
    answer = [[None for _ in range(n)] for _ in range(n)]
    steps = [(0,1),(1,0),(0,-1),(-1,0)]
    k = 1
    current_x = 0
    current_y = 0

    while(k <= pow(n,2)):

        for step in steps:
            dx , dy = step
            if(k > pow(n,2)):
                break
            while(0 <= current_x <= n - 1 and 0 <= current_y <= n -1):

                answer[current_x][current_y] = k

                k += 1
                if(k > pow(n,2)):
                    break
                
                current_x += dx
                current_y += dy

                if(current_y >= n ):
                    current_y -= 1
                    current_x += 1
                    break
                elif (current_x >= n):
                    current_x -= 1
                    current_y -= 1
                    break
                elif (current_x <= -1):
                    current_x += 1
                    current_y -= 1
                    break
                elif (current_y <= -1 ):
                    current_y += 1
                    current_x -= 1
                    break

                if(answer[current_x][current_y] is not None):
                    if(step == (-1,0)):
                        current_y += 1
                        current_x += 1
                        break
                    elif( step == (0,1)):
                        current_y -= 1
                        current_x += 1
                        break
                    elif( step == (1,0)):
                        current_x -= 1
                        current_y -= 1
                        break
                    elif( step == (0,-1)):
                        current_x -= 1
                        current_y += 1
                        break
    return answer

a =Arrange_integers(n)
for i in range(len(a)):
    print(a[i])



