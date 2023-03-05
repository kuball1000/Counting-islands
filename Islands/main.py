lines = int(input())
matrix = []
for i in range(lines):
    matrix.append(list(input()))

def found(k, x, y):
    matrix[x][y] = '2'
    if x + 1 < len(k) and k[x + 1][y] == '1':
        found(k, x + 1, y)
    if x - 1 >= 0 and k[x - 1][y] == '1':
        found(k, x - 1, y)
    if y + 1 < len(k) and k[x][y + 1] == '1':
        found(k, x, y + 1)
    if y - 1 >= 0 and k[x][y - 1] == '1':
        found(k, x, y - 1)

number_of_islands = 0
for i in range(lines):
    for j in range(lines):
        if matrix[i][j] == '1':
            found(matrix, i, j)
            number_of_islands += 1
print(number_of_islands)