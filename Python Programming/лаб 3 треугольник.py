from math import *
#input
print('координаты трех точек на плоскости:')
xa=float(input('xa='))
ya=float(input('ya='))
xb=float(input('xb='))
yb=float(input('yb='))
xc=float(input('xc='))
yc=float(input('yc='))
#
def leng(x1,y1,x2,y2):
    return sqrt(pow(x2-x1,2)+pow(y2-y1,2))
#
def square(x1,y1,x2,y2,x3,y3):
    a=leng(x1,y1,x2,y2)
    b=leng(x2,y2,x3,y3)
    c=leng(x3,y3,x1,y1)
    p=(a+b+c)/2
    return sqrt(p*(p-a)*(p-b)*(p-c))
#Найти длины стороны треугольника
a=leng(xb,yb,xc,yc)
b=leng(xc,yc,xa,ya)
c=leng(xa,ya,xb,yb)
print('длины стороны треугольника:')
print('AB=',c)
print('BC=',a)
print('CA=',b)
#найти длину высоты, проведенной изнаименьшего угла треугольника
s=square(xa,ya,xb,yb,xc,yc)
print('длину высоты, проведенной изнаименьшего угла треугольника:')
if a<b and a<c:
    print(2*s/a)
elif b<a and b<c:
    print(2*s/b)
else: print(2*s/c)
#
print('координат одной точки K:')
xk=float(input('xk='))
yk=float(input('yk='))
sk=square(xk,yk,xa,ya,xb,yb)+square(xk,yk,xb,yb,xc,yc)+square(xk,yk,xc,yc,xa,ya)
print(s)
print(sk)
if sk==s:
    print('точка K находиться внутри треугольник')
else: print('точка K находиться внешне треугольник')
