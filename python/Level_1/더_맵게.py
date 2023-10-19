import heapq

scoville = [1, 2, 3, 9, 10, 12]	
K = 7

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while(True):
        try:
            a = heapq.heappop(scoville)
            if(a < K):   #처음 요소가 K보다 작으면 다음 요소와 합산
                b = heapq.heappop(scoville)
                sum = a + b * 2
                heapq.heappush(scoville, sum)
                answer += 1 
            else:      # K보다 큰 값이면 while 문 종료
                break
        except IndexError:  # scoville이 비어졌으면 -1 출력
            return -1

    return answer

print(solution(scoville, K))