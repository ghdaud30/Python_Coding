n = 7
lost = [2,4]
reserve = [1,3]

def uniform(n, lost, reserve):
    count = 0
    total = []
    ex = []

    for i in range(1,n+1):
        if(i not in lost and i not in reserve):
            total.append(i)
    print(total)
    count += len(total)

    for i in reserve:
        if i in lost:
            continue
        else:
            count += 1

    for i in lost:

        pre = i - 1
        next = i + 1
        if(pre in reserve):
            count += 1
            reserve.remove(pre)
        elif(next in reserve):
            count += 1
            reserve.remove(next)
            
    return count

print(uniform(n, lost, reserve))