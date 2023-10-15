s = "123"

def solution(s):
    answer = ''
    word = ''
    
    number_dict = {'zero' : '0','one' : '1' ,'two' : '2','three' : '3',
    'four' : '4' ,'five' : '5'  ,'six' : '6','seven' : '7' ,'eight' : '8'
    ,'nine' : '9'}
    number_list = [str(i) for i in range(10)]
    result = []

    for letter in s:
        word += letter
        if(word in number_dict):
            result.append(number_dict[word])
            word = ''
        if(word in number_list):
            result.append(word)
            word = ''

    for i in result:
        answer += i

    answer = int(answer)

    print(result)

    return answer

print(solution(s))