
# name = ["may", "kein", "kain", "radi"]

# yearining = [5, 10, 1, 3]

# photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

# name = ["kali", "mari", "don"]

# yearning = [11, 1, 55]

# photo = [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]

def examine_dict(name, yearning, photo):
    dict = {name[i]: yearning[i] for i in range(len(name))}

    answer = []
    sums = [0 for i in range(len(photo))]

    for i in range(len(photo)):
        for j in range(len(photo[i])):
            if(photo[i][j] in dict.keys()):
                answer.append(dict[photo[i][j]])
                print(answer)
                sums[i] += sum(answer)
            answer.clear()
    print(sums)
    answer = sums
    print(answer)

    return answer

