bin1 = "10"
bin2 = "11"

def binary_number(bin1,bin2):
    answer = ''
    a =int(bin1,2)
    b = int(bin2,2)
    c = a + b
    d = bin(c)
    answer = d[2:]
    print(answer)
binary_number(bin1,bin2)
