from math import *
#input
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))

if a==0:
    if b==0:
        if c==0:
            print('бесконечность решения')
        else:
            print('нет решения')
    else:
        print('x=',-c/b)
else:
    t=pow(b,2)-4*a*c
    if t<0:
        print('нет решения')
    elif t==0:
        print('x=',-b/(2*a))
    else:
        print('x1=',(-b+sqrt(t))/(2*a))
        print('x1=',(-b-sqrt(t))/(2*a))
