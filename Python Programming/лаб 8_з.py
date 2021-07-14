from math import*
#input
def inputint(a):
    try:
        return int(input('Input ' + a + ': '))
    except ValueError:
        print('input errror')
        return(inputint(a))
def inputfloat(a):
    try:
        return float(input('Input ' + a + ': '))
    except ValueError:
        print('input errror')
        return(inputfloat(a))
a=inputfloat('a')
b=inputfloat('b')
n=inputint('n')
#program
def f(x):
    return(x*x)
def I(n):
    t=0
    h=(b-a)/n
    x = a
    for i in range(1,n+1):
        x += h
        t += f(x)
    t*=h
    return(t)
#output
print('метод правых прямоугольников: {:7g}'.format(I(n)))
