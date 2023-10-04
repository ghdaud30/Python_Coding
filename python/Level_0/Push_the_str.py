a = "abc"
b = "bca"

def push_the_str(A, B):

    answer = 0

    if(A == B):
        return answer

    for i in range(len(A)):
        last = A[-1]
        new = last + A[:-1]
        A = new
        if(A == B):
            answer += 1
            return answer
        else:
            answer += 1
    
    if( A != B):
        answer = -1
        return answer
        

    
print(push_the_str(a,b))