from typing import List, Tuple, Callable 

Matrix = List[List[float]]
Vector = List[float]

A = [[1,2,3],
     [4,5,6]]

B =[[1,2],
    [3,4],
    [5,6]]

#Numero de linhas = len(A), número de colunas = len(A[0])

def shape(A:Matrix)->Tuple[int,int]:
  """Retorna o número de linhas e de colunas de A"""
  num_rows = len(A)
  num_cols=len(A[0]) if A else 0
  return(num_rows,num_cols)

def get_row(A:Matrix,index: int)-> Vector:
  """Retorna a linha index de A, como um vetor"""
  return(A[index])

def get_col(A:Matrix, index:int)-> Vector:
  """Retorna a coluna index de A, como um vetor"""
  return [Ai[index] for Ai in A]

def make_matrix(num_rows:int, num_cols:int, entry_function:Callable[[int,int],float])->Matrix:
  """Retorna uma matrix num_rows X num_cols cuja entrada (i,j) é entry_function(i,j)"""
  return[[entry_function(i,j) for j in range(num_cols)] for i in range (num_rows)]
  # com i, cria uma lista [entry_function(i,0), ...] para cada i

def identity_matrix(n: int)-> Matrix:
  """Retorna matriz identidade de tamanho n"""
  return make_matrix(n,n, lambda i, j:1 if i==j else 0 )
