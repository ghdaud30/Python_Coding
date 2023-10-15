array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


def solution(array, commands):
    answer = []

    for command in commands:
    #for i,j,k in commands:
    
        i = command[0]
        j = command[1]
        k = command[-1]
        new_array = array[i-1:j]
        new_array.sort()

        find_num = new_array[k-1]

        answer.append(find_num)

    return answer

print(solution(array, commands))