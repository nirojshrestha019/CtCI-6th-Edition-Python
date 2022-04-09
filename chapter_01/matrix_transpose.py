# Transpose list of lists
# l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# r = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]



def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))

l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
r = transpose_matrix(l)
print(r)
# r = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
