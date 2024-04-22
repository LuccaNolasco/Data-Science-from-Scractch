from collections import Counter
from matplotlib import pyplot as plt
import random

num_friends=[random.randint(0,100) for _ in range (300)]

friend_counts= Counter(num_friends)
xs = range(101) #O maior valor é 100
ys = [friend_counts[x] for x in xs] #A altura indica o número de amigos
plt.bar(xs,ys)
plt.axis([0,101,0,25])
plt.title("Histograma da Contagem de amigos")
plt.xlabel("N° de amigos")
plt.ylabel("N° de pessoas")
plt.show()

num_points= len(num_friends) #Quantidades de valores na lista, provavelmente 300
largest_value=max(num_friends)
smallest_value=min(num_friends)

print("Num points: " + str(num_points))
print("Maior valor: "+ str(largest_value))
print("Menor valor: "+ str(smallest_value))