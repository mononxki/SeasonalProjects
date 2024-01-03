
def seq(n):
    res = []
    for i in range(2, n * 3, 3):
        res.append(i)
    return res

n = int(input("Provide the N-value to stop at:  "))
print(seq(n))


# Counting values for sequence: 2, 5, 8, 14, 17, ... 
