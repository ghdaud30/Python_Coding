numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

def solution(numbers, hand):
    answer = ''
    left = 0
    right = 0

    for i in numbers:
        if(i == 1 or i == 4 or i == 7):
            answer += 'L'
            left = i
        elif(i == 3 or i == 6 or i== 9):
            answer += 'R'
            right = i
        else:
            if(abs(i - left) < abs(i - right)):
                answer += 'L'
                left = i
            elif(abs(i - left) > abs(i - right)):
                answer += 'R'
                right = i
            else:
                if(hand == 'left'):
                    answer += 'L'
                else:
                    answer += 'R'

    return answer

print(solution(numbers, hand))