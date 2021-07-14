from math import*
#input
def inputint(a):
    try:
        print('input',a)
        return int(input())
    except ValueError:
        print('input errror')
        return(inputint(a))
def inputfloat(a):
    try:
        print('input',a)
        return float(input())
    except ValueError:
        print('input errror')
        return(inputfloat(a))
a=inputfloat('a')
b=inputfloat('b')
n1=inputint('n1')
n2=inputint('n2')
e=inputfloat('e')
#program
def f1(x):
    return 2*x+5
def f(x):
    return x**2 + 5*x
def metod1(n):
    t=0
    h=(b-a)/n
    for i in range(n):
        x=a+h*i
        t+=f(x)
    t*=h
    return(t)
def metod2(n):
    t=0
    h=(b-a)/n
    for i in range(1,n):
        x=a+h*i
        t+=f(x)
    t+=(f(a)+f(b))/2
    t*=h
    return(t)
#output
print('-'*74)
print('|{:^30}|{:^20}|{:^20}|'.format('n',n1,n2))
print('-'*74)
print('|{:^30}|{:^20.9g}|{:^20.9g}|'.format('метод левых прямоугольников:',metod1(n1),metod1(n2)))
print('-'*74)
print('|{:^30}|{:^20.9g}|{:^20.9g}|'.format('метод трапеций:',metod2(n1),metod2(n2)))
print('-'*74)
#
I=f1(b)-f1(a)
m=max(abs(metod1(n1)-I),abs(metod1(n2)-I),abs(metod2(n1)-I),abs(metod2(n2)-I))
if round(abs(metod1(n1)-I)-m,20)==0 or round(abs(metod1(n2)-I)-m,20)==0:
    n1=1
    s1=metod1(n1)
    ok=True
    while ok:
        s2=metod1(2*n1)
        if abs(s2-s1)<e:
            ok=False
        s1=s2
        n1*=2
    print('метод левых прямоугольников: ',end='')
    print('n=',n1)
    print('I=',s2)
else:
    n2=1
    s1=metod2(n2)
    ok=True
    while ok:
        s2=metod2(2*n1)
        if abs(s2-s1)<e:
            ok=False
        s1=s2
        n2*=2
    print('метод трапеций:')
    print('n=',n2)
    print('I=',s2)
