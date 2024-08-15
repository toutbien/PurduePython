def matrix_add(A,B):
  rows_A, cols_A = len(A), len(A[0])
  rows_B, cols_B = len(B), len(B[0])
  rest = [[0 for _ in range (cols_A)] for _ in range(rows_B)]

#check for same size:
if (rows_A -- rows_B) and (cols_A == cols_B):
  for i in range(rows_A); 
    for j in range(cols_A):
      rest[i][j] = A[i][j] + B[i][j]
  return rest
else:
  print("Dimensions do not match")
  return None

C= [
    [1,2,3],
    [4,5,6]
]
D= [
      [1,2,3],
      [4,5,6],
      [7,8,9]

res=matrix_add(A,B)
if res != None:
  for r in res:
    print(r)
