n = 5
words = 	["hello", "observe", "effect", "take", "either", "recognize"
          , "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]

def solution(n, words):
    answer = []
    word_list = []
    user_dic = {i : 0 for i in range(n) }
    count = 0

    for idx ,word in enumerate(words):
        if(count >= n):
            count %= n

        if(len(word_list) >= 1):
            if(word[0] != word_list[-1][-1]):
                count += 1
                user_dic[idx % n] += 1
                answer.append((idx % n) + 1)
                answer.append(user_dic[idx % n])
                break

        if(word not in word_list):
            word_list.append(word)
            count += 1
            user_dic[idx % n] += 1
        else:
            count += 1
            user_dic[idx % n] += 1
            answer.append((idx % n) + 1)
            answer.append(user_dic[idx % n])
            break

    if(len(answer) == 0):
        return [0,0]

    return answer

print(solution(n,words))