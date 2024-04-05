import numpy

def f(x):
    return (2*(x**3) - 11.7*(x**2) + 17.7*x -5)

def g1(x):
    return ((11.7*(x**2) - 17.7*x + 5)/2)**(1/3)

def g2(x):
    return ((-2*(x**3) - 17.7*x + 5)/(-11.7))**(1/2)
    
def g3(x):
    return ((-2*(x**3) + 11.7*(x**2) + 5)/17.7)

e = 1
x = 2
x1 = 0

vet = [x]
vet1 = [x]
vet2 = [x]

while e > 0.0001:
    x1 = g1(x)
    e = numpy.abs((x1-x)/x1)
    x = x1
    vet.append(x1)


x = 2
e = 1

while e > 0.0001:
    x1 = g2(x)
    e = numpy.abs((x1-x)/x1)
    x = x1
    vet1.append(x1)

    
x = 2
e = 1

while e > 0.0001:
    x1 = g3(x)
    e = numpy.abs((x1-x)/x1)
    x = x1
    vet2.append(x1)


print("xi      |g1(x) |g2(x) |g3(x)")

for i in range(max(len(vet),len(vet1), len(vet2))):
    print(f'x{i}      ',end='|')
    if i < len(vet):
        print(f'{vet[i]:.4f}',end='|')
    else:
        print("------",end='|')
    if i < len(vet1):
        print(f'{vet1[i]:.4f}',end='|')
    else:
        print("------",end='|')
    if i < len(vet2):
        print(f'{vet2[i]:.4f}')
    else:
        print("------")
