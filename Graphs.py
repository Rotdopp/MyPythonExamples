from collections import defaultdict

n = 8

A = [[0,1], [1,2], [0,3], [3,4], [3,6], [3,7], [4,2], [4,5], [5,2]]

print(A)

M = []
for i in range(n): # Adjacency Matrix
    M.append([0] * n)

for u, v in A: # Adjacency Matrix
    M[u][v] = 1

print(M)

#-----------------------------------

D = defaultdict(list) #  Adjacency List
for u, v in A:
    D[u].append(v)
print(D)
print(D[3]) # what 3 points to