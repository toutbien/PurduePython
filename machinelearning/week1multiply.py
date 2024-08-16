def matrix_multiplication(A,B):
  rows_A, cols_A = len(A), len(A[0])
  rows_B, cols_B = len(B), len(B[0])
  rest = [[0 for _ in range (cols_B)] for _ in range(rows_A)]

  if cols_A != rows_B:
    print("Dimensions are not a match")
    return None
  else:
    for i in range(rows_A):
      for j in range(cols_B):
        for k in range(cols_A):
          rest[i][j] += A[i][k] * B[k][j]
    return rest


T = [[3, 5, 9], [1, 2, 3]] 
N = [[6, 2], [3, 8], [4, 1]]
res = matrix_multiplication(T,N)
if res != None:
  for r in res:
    print(r)
