from matplotlib import pyplot as plt

notas_teste_1=[99,90,85,97,80]
notas_teste_2=[100,85,60,90,70]

plt.scatter(notas_teste_1,notas_teste_2)
plt.title("Os eixos não estão comparáveis")
plt.xlabel("notas do teste 1")
plt.ylabel("notas do teste 2")

#Até aqui o gráfico fica com uma formatação estranha, e póde enganar o leitor
plt.show()

#Agora fica mais condizente, e percebe-se que a maior variação foi na prova 2
plt.scatter(notas_teste_1,notas_teste_2)
plt.title("Os eixos não estão comparáveis")
plt.xlabel("notas do teste 1")
plt.ylabel("notas do teste 2")
plt.axis("equal")
plt.title("Os eixos estão devidamente comparáveis")
plt.show()