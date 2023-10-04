import random
import copy

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

def 로또최고최저순위(lottos,win_nums):
    max_lottos = copy.deepcopy(lottos)
    min_lottos = copy.deepcopy(lottos)
    count_max = 0
    count_min = 0
    rank_max = 0
    rank_min = 0
    result = []

    lottos.sort()
    win_nums.sort()

    if(all(x == y for x , y in zip(lottos,win_nums))):
        rank_max = 1
        rank_min = 1
        result.append(rank_max)
        result.append(rank_min)
        return result
    else:
        print(max_lottos)
        print(min_lottos)

        for i in range(len(win_nums)):
            for j in range(len(lottos)):
                if(max_lottos[j] == 0 and win_nums[i] not in max_lottos):
                    max_lottos[j] = win_nums[i]

        min_random = [x for x in range(1,46) if x not in win_nums]
        for i in range(len(win_nums)):
            if (min_lottos[i] == 0):
                number = random.choice(min_random)
                min_lottos[i] = number
                min_random.remove(number)

        max_lottos.sort()
        min_lottos.sort()
        print(win_nums)
        print(max_lottos)
        print(min_lottos)

        for i in range(len(win_nums)):
            for j in range(len(lottos)):
                if(win_nums[i] == max_lottos[j]):
                    count_max += 1
                if(win_nums[i] == min_lottos[j]):
                    count_min += 1

        if(count_max == 2): rank_max = 5
        elif(count_max == 3): rank_max = 4
        elif(count_max == 4): rank_max = 3
        elif(count_max == 5): rank_max = 2
        elif(count_max == 6): rank_max = 1
        else: rank_max = 6

        if(count_min == 2): rank_min = 5
        elif(count_min == 3): rank_min = 4
        elif(count_min == 4): rank_min = 3
        elif(count_min == 5): rank_min = 2
        elif(count_min == 6): rank_min = 1
        else: rank_min = 6

        result.append(rank_max)
        result.append(rank_min)
        print(count_max)
        print(count_min)
        print(rank_max)
        print(rank_min)

        return result
    

print(로또최고최저순위(lottos,win_nums))


















lottos2 = [44, 1, 0, 0, 31, 25]
win_nums2 = [31, 10, 45, 1, 6, 19]


rank = [6,6,5,4,3,2,1]
zeros = lottos.count(0)
same = 0

for i in lottos2:
        if i in win_nums2:
            same += 1

max = zeros + same
min = same

print([rank[max],rank[min]]) 