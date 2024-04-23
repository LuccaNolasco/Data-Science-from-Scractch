from matplotlib import pyplot as plt

friends = [70,65,72,63,71,64,60,64,67]
minutes =[175,170,205,120,220,130,105,145,190]
rotulos = ['a','b','c','d','e','f','g','h','i']

plt.scatter(friends,minutes) #Irá comparar os dados

#Rotular cada ponto
for rotulo,friend_count,minute_count in zip(rotulos,friends,minutes):
  plt.annotate(rotulo,
               xy=(friend_count,minute_count), #Coloca o rótulo no respectivo ponto
               xytext=(5,-5), #Mas levemente delocado
               textcoords="offset points")
plt.title("Minutos Diários x Número de Amigos")
plt.xlabel("N° de amigos")
plt.ylabel("minutos diários gastos no site")
plt.show()