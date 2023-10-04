board = [[0,0,0,0,0],
         [0,0,1,0,3],
         [0,2,5,0,1],
         [4,2,4,4,2],
         [3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def 크레인_인형뽑기_게임(board,moves):
    answer = 0
    stack = []

    for i in moves:
        for j in range(len(board)):
            current = board[j][i-1]
            if(current != 0):

                if(len(stack)):
                    stack_pop = stack.pop()
                    if(stack_pop == current):
                        answer += 2
                    else:
                        stack.append(stack_pop)
                        stack.append(current)
                else:
                    stack.append(current)
                    
                board[j][i-1] = 0
                break

    return answer




print(크레인_인형뽑기_게임(board,moves))