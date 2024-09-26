def get_matrix(n, m, value):
    matrix= []
    if n > 0 and m > 0:
        for i in range(n):
            matrix.append([])
            for j in range(m):
                    matrix[i].append(value)
    return matrix
a=get_matrix(0, 7, 10)
print(a)
