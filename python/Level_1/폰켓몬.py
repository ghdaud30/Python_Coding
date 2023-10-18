nums = [3,3,3,2,2,2]	

def solution(nums):
    answer = 0
    pocketmon = {}
    count = 0

    for i in nums:
        if(i in pocketmon):
            pocketmon[hash(i)] += 1
        else:
            pocketmon[hash(i)] = 1

    for k , v in pocketmon.items():
        if(count == len(nums) // 2):
            break
        if(v > 1):
            v = 1
            answer += 1
            count += 1
        else: 
            answer += 1
            count += 1

    return answer

print(solution(nums))