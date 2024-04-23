from matplotlib import pyplot as plt

#years = [1950, 1960,1970,1980,1990,2000,2010]
years = [x for x in range (1950, 2011,10) ] # Loop de 1950 a 2011, pulando de 10 em 10
gdp = [300.2,543.3,1075.9,2862.5,5979.6,10289.7,14958.3]

#Crie um gráfico de linhas, ano no eixo x, gdp no eixo y
plt.plot(years,gdp,color='green',marker ='o',linestyle = 'solid')

#Crie um título
plt.title("Produto Interno Bruto Nominal")

#Adicione um rótulo ao eixo y
plt.ylabel("Bilhões de Dólares")
plt.show()

