import math as m
import numpy as np
import matplotlib.pyplot as plt

#Entrada da função
def f(x):
    return m.log10(x) + 3*m.sin(x/2)
#-----------------


#x1 = int(input("Valor inicial: "))
#x2 = int(input("Valor final: "))
#inter = int(input("Intervalo: "))

x1 = 4
x2 = 11
inter = 100


#criação do grafico seccionado
xAxis = np.linspace(x1, x2, inter)
yAxis = np.zeros(inter)

raizes = []

for i in range(len(xAxis)):
    yAxis[i] = f(xAxis[i])
#-----------------


#Validando os valores
for i in range(1, len(yAxis)):
    if yAxis[i]*yAxis[i-1] < 0:
        raizes.append(i)
#-----------------


#plotagem grafica
plt.plot(xAxis, yAxis)
plt.plot([x1,x2], [0,0], color = 'black')
plt.axis([x1, x2, min(yAxis), max(yAxis)])
plt.title('Grafico atividade 1', color = 'red')

#print dos resultados e plotagem dos pontos
for i in raizes:
    print("[y:{}, x:{}]".format(f(((xAxis[i]+xAxis[i-1])/2)),(xAxis[i]+xAxis[i-1])/2))
    plt.plot((xAxis[i]+xAxis[i-1])/2,f(((xAxis[i]+xAxis[i-1])/2)),marker = 'X',color = 'red')
#-----------------
    
plt.xlabel('Eixo x', color = 'red')
plt.ylabel('Eixo y', color = 'red')
plt.show()
#-----------------