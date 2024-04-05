import math as m
import numpy as np
import matplotlib.pyplot as plt

#Entrada da função
def f(x):
    return m.log10(x) + 3*m.sin(x/2)
#-----------------


#x1 = int(input("Valor inicial: "))
#x2 = int(input("Valor final: "))
#e = float(input("Erro valido: "))

x1 = 4
x2 = 11
e = 0.0001


#criação do grafico seccionado
xAxis = np.linspace(x1, x2, 100)
yAxis = np.zeros(100)

for i in range(len(xAxis)):
    yAxis[i] = f(xAxis[i])
#-----------------


#validando os valores
xl = x1
xu = x2
while np.abs(xl-xu)/np.abs(xl) > e:
    if f(xl)*f((xl+xu)/2) < 0:
        xu = (xl+xu)/2
    elif f(xu)*f((xl+xu)/2) < 0:
        xl = (xl+xu)/2
        
x = (xl+xu)/2
#-----------------


#plotagem grafica
plt.plot(xAxis, yAxis)
plt.plot([x1, x2], [0,0], color = 'black')
plt.axis([x1, x2, min(yAxis), max(yAxis)])
plt.title('Grafico atividade 1', color = 'red')

#print dos resultados e plotagem dos pontos
print("[y:{}, x:{}]".format(f(x),x))
plt.plot(x, f(x), marker = 'X',color = 'red')
#-----------------

plt.xlabel('Eixo x', color = 'red')
plt.ylabel('Eixo y', color = 'red')
plt.show()
#-----------------