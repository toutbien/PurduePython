def matrix_subtraction(A,B):
  rows_A, cols_A = len(A), len(A[0])
  rows_B, cols_B = len(B), len(B[0])
  rest = [[0 for _ in range (cols_A)] for _ in range(rows_B)]

#CODE HERE 
if (rows_A == rows_B) and (cols_A == cols_B_
  for i in range(rows_A):
    for j in range(cols_A):
      = A[i][j]

return rest

X = [[12,7,3],
     [4,5,6],
     [7,8,9]]
Y = [[5,8,1],
     [6,7,3],
     [4,5,9]]
res = matrix_subtraction(X,Y)
for r in res:
  print(r)
