survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]	

def Take_a_personality_test(survey, choices):
    answer = ''
    score = [3,2,1,0,1,2,3]
    result = {}
    result2 = [{'R': 0, 'T':0},{'C':0,'F':0},{'J':0,'M':0},{'A':0,'N':0}]

    for i in range(len(survey)):
        for j in range(len(result2)):
            if(choices[i]-1 > score.index(0)):
                if survey[i][1] in result2[j]:
                    result2[j][survey[i][1]] += score[choices[i]-1]
            else:
                if survey[i][0] in result2[j]:
                    result2[j][survey[i][0]] += score[choices[i]-1]
    
    print(result2)

    for i in range(len(result2)):
        list_key = list(result2[i].keys())
        list_value = list(result2[i].values())

        if(list_value[0] > list_value[1]):
            answer += list_key[0]
        elif(list_value[0] < list_value[1]):
            answer += list_key[1]
        else:
            if(list_key[0] > list_key[1]):
                answer += list_key[1]
            else:
                answer += list_key[0]

    # for i in range(len(survey)):

    #     if(choices[i]-1 >= score.index(0)):

    #         if(survey[i][1] in result):
    #             result[survey[i][1]] += score[choices[i]-1]
    #         else:
    #             result[survey[i][1]] = score[choices[i]-1]
    #             result[survey[i][0]] = 0

    #     else:
    #         if(survey[i][0] in result):
    #             result[survey[i][0]] += score[choices[i]-1]
    #         else:
    #             result[survey[i][0]] = score[choices[i]-1]
    #             result[survey[i][1]] = 0

    # result_list = [[k, v] for k ,v in result.items()]
    # print(result_list)

    # for i in range(0, len(result_list),2):

    #     if(result_list[i][1] > result_list[i+1][1]):
    #         answer += result_list[i][0]
    #     elif(result_list[i][1] < result_list[i+1][1]):
    #         answer += result_list[i+1][0]
    #     elif (result_list[i][1] == result_list[i+1][1]):
    #         if(result_list[i] > result_list[i+1]):
    #             answer += result_list[i+1][0]
    #         else:
    #             answer += result_list[i][0]
            
    return answer

print(Take_a_personality_test(survey,choices))