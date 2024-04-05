import numpy

def f(x):
    return numpy.sin(x/2)*numpy.log10(-10*x)
    
x = -8
lamb = 10**(-6)
e = 1
x1 = 0
vet = [x]


while e > 0.0001:
    x1 = x-((lamb*x*f(x))/(f(x+lamb*x)-f(x)))
    e = numpy.abs((x1-x)/x1)
    x = x1
    vet.append(x1)


print("xi   |Valores")
for i in range(len(vet)):
    print(f'x{i}   |{vet[i]:.4f}')