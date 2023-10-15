n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = 	[30, 1, 21, 17, 28]

def solution(n, arr1, arr2):
    arr3 = []
    arr4 = []
    answer = []
    sentence = ''

    for i , v in zip(arr1, arr2):
        a = list(bin(i)[2:].zfill(len(arr1)))

        arr3.append(a)
            
        b = list(bin(v)[2:].zfill(len(arr2)))
        arr4.append(b)


    for i in range(len(arr3)):
        for j in range(len(arr3[0])):
            if(arr3[i][j] == '1' or arr4[i][j] == '1'):
                sentence += '#'
            if(arr3[i][j] == '0' and arr4[i][j] == '0'):
                sentence += ' '
        answer.append(sentence)
        sentence = ''  

    return answer

print(solution(n, arr1, arr2))