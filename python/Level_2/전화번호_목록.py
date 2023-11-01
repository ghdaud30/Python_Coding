phone_book = ["12","123","1235","567","88"]

def solution(phone_book):
    answer = True
    # 문자열 리스트를 작은크기부터 정렬해줍니다
    phone_book.sort()
    print(phone_book)
    
    # 그후 자기 값과 다음 값을 비교하여 
    # 현재값이 다음값에 접두사인지 확인합니다
    for i in range(len(phone_book)):
        try:
            pre = len(phone_book[i])
            if(phone_book[i] in phone_book[i+1][:pre]):
                return False
        except IndexError:
            pass

    return answer

print(solution(phone_book))