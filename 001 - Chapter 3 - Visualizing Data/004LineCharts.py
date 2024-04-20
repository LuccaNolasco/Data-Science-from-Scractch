from matplotlib import pyplot as plt
#Gráficos em linha são ótimos para mostrar tendências

variance = [2**i for i in range(9)]
bias_squared = variance[::-1]
total_error = [x+y for x,y in zip(variance,bias_squared)]
xs=[i for i, _ in enumerate (variance)] 

#Podemos fazer múltiplas chamadas para plt.plot para mostrar múltiplas séries no mesmo gráfico
plt.plot(xs,variance,'green',label='variance') #linha verde sólida
plt.plot(xs, bias_squared,"r-.",label='bias^2') #linha vermelha tracejada
plt.plot(xs, total_error,"b:",label="total error")

#Como atribuímos rótulos a cada série, podemos criar uma legenda (loc = 9 significa "top center")
plt.legend(loc='best')
plt.xlabel("Complexidade do modelo")
plt.xticks( [x for x in range(len(variance))] )
plt.title("O Dilema Viés-Variância")

plt.show()

