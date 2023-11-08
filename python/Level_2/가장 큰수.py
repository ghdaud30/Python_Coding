numbers = [9,900,91,3,4]

def solution(numbers):
    answer = ''
    num = []

    if all(number == 0 for number in numbers):
        return '0' 
    
    # 첫째 자리 숫자를 비교할려고 합니다
    # 첫째 자리가 같은 숫자를 비교하기 위해 
    # 오름차순 해줍니다 )3,30,300
    numbers.sort()
    

    
    # 그 후 모두 네자리수 숫자로 맞춰주고
    # 리스트에 담아줍니다
    for number in numbers:
        if(number < 1000):
            if(number < 10):
                num.append(str(number) + '000')
            elif(10 <= number < 100):
                num.append(str(number) + '00')
            else:
                num.append(str(number) + '0')
        else:
            num.append(str(number))

    # 내림차순 하여서 인덱스 값을 구합니다
    num = sorted(enumerate(num), key = lambda x : x[1], reverse = True)

    # 기존 리스트에 인덱스를 넣어 answer 값을 구해줍니다
    for i in num:
        answer += str(numbers[i[0]])

    print(num)

    return answer

print(solution(numbers))