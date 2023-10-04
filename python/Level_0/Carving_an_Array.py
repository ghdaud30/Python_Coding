arr = [2,3,4,5,6,7,8]
query = [4, 2, 1]

def Carving_an_Array(arr,query):
    answer = []

    for i in range(len(query)):
        if(i % 2 == 0):
            del arr[query[i] + 1:]
        else:
            del arr[:query[i]]
    answer = arr
    
    return answer

print(Carving_an_Array(arr,query))