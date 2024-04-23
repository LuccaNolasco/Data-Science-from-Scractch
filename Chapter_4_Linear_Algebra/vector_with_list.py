import math
from typing import List

#Importamos List[Float] de typing, para fazer anotações de tipo
#Aqui apenas indicamos que um vetor é uma lista de números reais
Vector = List[float]

height_weight_age=[70,170,40] #Polegadas, libras, anos
grades =[95,80,75,62] #Representa os testes
#Lists não são vetores, o que dificulta as operações. Por isso, irei construir essas ferramentas aritméticas


def add(v: Vector, w: Vector) -> Vector:
  """Soma os elementos correspontendes"""
  assert len(v) == len(w), "vetores devem ter o mesmo tamanho"
  return[vi + wi for vi,wi in zip(v,w)]

def subtract(v: Vector, w: Vector) -> Vector:
  """Subtração de elementos correspondentes"""
  assert len(v)==len(w), "Vetores devem ter o mesmo tamanho"
  return[vi - wi for vi,wi in zip(v,w)]

# Às vezes, é preciso somar uma lista de vetores por componente
# Para isso, criaremos uym método que vá somando tudo
def vector_sum(vectors: List[Vector]) -> Vector:
  """Soma todos os vetores"""
  assert vectors , "sua lista está vazia"
  num_elements=len(vectors[0])
  assert all(len(vectors)) == num_elements , "É preciso que o tamanho seja o mesmo"
  return[sum(vector[i] for vector in vectors ) for i in range(num_elements)]

def scalar_multiply(c: float, v:Vector)-> Vector:
  """Retorna um vetor multiplicado pelo escalar"""
  return[c*vi for vi in v]

def vector_mean(vectors: List[Vector])-> Vector:
  """Computa a media"""
  numOfVectors = len(vectors)
  return scalar_multiply(1/numOfVectors, vector_sum(vectors))

#Produto escalar (dot product) = multiplicamos as posições correspondesntes e somamos com o resto
#Exemplo (1,2,3) dot (4,5,6) = 1*4 + 2*5 + 3*6
def dot(v: Vector, w: Vector)-> float:
  """Retorna o produto escalar"""
  assert len(v)==len(w), "Vetores precisam ter o mesmo tamanho"
  return sum(vi*wi for vi,wi in zip(v,w))

def sum_of_squares(v: Vector)-> float:
  """Retorna v1*v1 + v2*v2 ... + vn*vn"""
  return dot(v,v)

def magnitude(v: Vector)-> float:
  """Retorna o módulo do vetor"""
  return math.sqrt(sum_of_squares(v))

#Agora, temos tudo o que precisamos para computara distância entre dois vetores, de duas formas:
#Assim:

def squared_distance(v: Vector, w: Vector)->float:
  """Retorna (v1-w1)^2 +...+(vn-wn)^2"""
  return sum_of_squares(subtract(v,w))

def distance(v: Vector, w:Vector)-> float:
  """Retorna a distância"""
  return math.sqrt(squared_distance(v,w))

#Ou assim:
def distance(v:Vector, w:Vector)-> float:
  return magnitude(subtract(v,w))
  
#Esses métodos não são eficientes, e serão usados apenas como didática
