import sys
sys.path.append('./')
from Chapter_4_Linear_Algebra.vector_with_list import sum_of_squares, dot

from collections import Counter
from matplotlib import pyplot as plt
from typing import List
import random
from Chapter_4_Linear_Algebra.vector_with_list import sum_of_squares
import math

num_friends=[random.randint(0,100) for _ in range (300)]
daily_minutes = [random.randint(5,150) for _ in range(300)] 

#---------------------------------------------------------
# CENTRAL TENDENCIES


def mean(list: List[float]) -> float:
  return sum(list)/len(list)

#O sublinhado indica que as funções são "Privadas", e não devem ser chamadas por
#outros usuário, apenas pela própria função mediana

def _median_odd(list : List[float]) -> float:
  """Se len(list) for impar, a mediana será o valor do meio"""
  return sorted(list)[len(list)//2]

def _median_even(list : List[float]) -> float:
  """Se len(list) for par, a mediana será a média de ambas do meio"""
  sorted_list = sorted(list) #Como será usado duas vezes, achei por bem salvar em outra lista para não ordenar 2x
  tam = len(list) # Mesma coisa. Para não contar 2x
  return ( sorted_list[tam//2] + sorted_list[(tam//2)-1] ) / 2

def median(list: List[float]) -> float:
  """Encontra a media de list"""
  return _median_even(list) if len(list)%2 == 0 else _median_odd(list)

#Uma generalização da mediana é o QUANTIL, que separa uma determinada porcentagem dos dados (a mediana separa 50% dos dados)

def quantile(list : List[float], p: float) -> float:
  """Retorna o valor p-ésimo em x"""
  p_index = int(p*len(list))
  return sorted(list)[p_index]

def mode(list : List[float]) -> List[float]:
  """Retorna uma lista com os valores mais repetidos. Pode haver mais de um"""
  counts = Counter(list)
  max_count = max(counts.valuues())
  return[xi for xi,count in counts.items() if count == max_count]

# -----------------------------
# DISPERSÃO
# ----------------------------

#Amplitude
def data_range(list : List[float]) ->float:
  return max(list) - min(list)

def de_mean(list: List[float]) -> List[float]:
  """Percorre a lista e subtrai a média de cada um dos valores"""
  listMean = mean(list)
  return[x - listMean for x in list]

def variance(list: List[float]) -> float:
  """Quase o desvio quadrado médio"""
  assert len(list) >=2 , "variância precisa de ao menos 2 valores"
  tam = len(list)
  desvios = de_mean(list)
  return sum_of_squares(desvios) / (tam-1)

def standard_deviation(list : List[float]) -> float:
  """O desvio padrão é a raiz quadrada da variância"""
  return math.sqrt(variance(list))

def interquartile_range(list : List[float]) -> float:
  """Retorna a diferença entre o percentil 75% e o percentil 25%"""
  return quantile(list,0.75) - quantile(list,0.25)

def covariance(list1: List[float],list2: List[float]) -> float:
  assert len(list1) == len(list2) , "ambas listas precisam ter a mesma quantidade de elementos"
  return dot(de_mean(list1), de_mean(list2)) / (len(list1) - 1)

def correlation(list1: List[float], list2: List[float]) -> float:
  """Mede a variação simultânea de X e Y, tendo -1 e 1 como máximo e mínimo"""
  devPad_1 = standard_deviation(list1)
  devPad_2 = standard_deviation(list2)
  if devPad_1 > 0 and devPad_2> 0:
    return covariance(list1, list2)/ devPad_1/devPad_2  # equivalente a / (devPad_1 * devPad_2)
  else:
    return 0 # se não houver desvio padrão (variação), a correlação será zero.
  
