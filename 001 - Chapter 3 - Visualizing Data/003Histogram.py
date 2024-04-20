from matplotlib import pyplot as plt
from collections import Counter

grades = [83,95,91,70,0,85,82,100,67,73,77,0]

#Agrupe as notaas em dezenas, e coloca o 100 com o 90
histogram = Counter(min(grade//10*10,90)for grade in grades) 
#Grade será inteiramente dividido // por 10, e depois multiplicado, logo retornará a dezena anterior. Isso até 90
#pois 100 estará na mesma barra do 90. Em suma, fará 10 barras começando de cada dezena, do 0 ao 90
#O min retorna o valor mínimo após toda essa lógica (no caso, 0)

plt.bar([x+5 for x in histogram.keys()], # move as barras para a direita em 5
         histogram.values(),             # atribui a altura correta a cada barra 
         10,                             #Atribue a largura 10 a cada barra 
         edgecolor=(0,0,0))              #Escurece as bordas das barras 

plt.axis([-5,105,0,5])  #eixo x de -5 a 105, eixo y de 0 a 5

plt.xticks([10*i for i in range(11)])  #rótulos do eixo x em 0, 10, 20...
plt.xlabel("Dezenas")
plt.ylabel("N° de alunos")
plt.title("Distribuição das notas do Exame 1")
plt.show()