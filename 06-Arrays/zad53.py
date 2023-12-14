def identity_matrix(n):
    result_matrix = []

    for i in range(0, n):
        row = []
        for j in range(0, n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        result_matrix.append(row)
    return result_matrix

def display(matrix):
    for row in matrix:
        print(*row)

n = 3
result_matrix = identity_matrix(n)
display(result_matrix)