from matplotlib import pyplot as plt

movies =["Annie Hall","Ben-Hur","Casablanca","Ghandi","West Side Story"]
num_oscars=[5,11,3,8,10]

#Imprima as barras com coordenadas x à esquerda [0,1,2,3,4], alturasa [num_oscars]
plt.bar(range(len(movies)),num_oscars)

plt.title("Filmes com Oscar")
plt.ylabel("N° de Oscars")

#rotule o eixo x com os nomes dos filmes nos centros das barras
plt.xticks(range(len(movies)),movies)

plt.show()
