def get_matrix(n, m, value):
    matrix= []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix
a=get_matrix(2, 7, 10)
print(a)
