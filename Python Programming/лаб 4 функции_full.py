from math import *
xn=float(input('{:20}'.format('начальная точка:')))
xk=float(input('{:20}'.format('конечная точка:')))
s=float(input('{:20}'.format('шаг:')))
#таблица значении функции
print('таблица значении функции:')
print('-'*55)
print('|',' '*6,'x',' '*6,'|',' '*6,'y1',' '*5,'|',' '*6,'y2',' '*5,'|')
print('-'*55)
x=xn
while x<=xk:
    h1=pow(x,2)+4*sin(x)
    h2=exp(x)+exp(-15*x)-4
    print('|','{:15.5g}'.format(x),'|','{:15.5g}'.format(h1),'|','{:15.5g}'.format(h2),'|')
    print('-'*55)
    x=x+s
#функция 1
print('x'*80)
print('график функции 1:')
ymin=ymax=pow(xn,2)+4*sin(xn)
x=xn
while x<=xk:
    y=pow(x,2)+4*sin(x)
    ymin=min(ymin,y)
    ymax=max(ymax,y)
    x=x+s
l=abs(round(ymin/(ymax-ymin)*80))
x=xn
if ymin<0:
    while x<=xk:
        y=pow(x,2)+4*sin(x)
        h=round(abs(((y-ymin)/(ymax-ymin)))*80)
        if round(x,8)==0:
            print('-'*(h+1),'*','-'*(80-h+1),sep='')
        else:
            if y>0:
                print(' '*(l+1)+'|'+' '*(h-l)+'*',sep='')
            else:
                print(' '*(h)+'*'+' '*(l-h)+'|',sep='')
        x=x+s
else:
    while x<=xk:
        y=pow(x,2)+4*sin(x)
        h=round(abs(((y-ymin)/(ymax-ymin)))*80)
        if round(x,8)==0:
            print('-'*(h+1),'*','-'*(80-h+1),sep='')
        else:
            print('|'+' '*h+'*',sep='')
        x=x+s        
#функция 2
print('x'*80)
print('график функции 2:')
ymin=ymax=exp(xn)+exp(-15*xn)-4
x=xn
while x<=xk:
    y=exp(x)+exp(-15*x)-4
    ymin=min(ymin,y)
    ymax=max(ymax,y)
    x=x+s
l=abs(round(ymin/(ymax-ymin)*80))
x=xn
if ymin<0:
    while x<=xk:
        y=exp(x)+exp(-15*x)-4
        h=round(abs(((y-ymin)/(ymax-ymin)))*80)
        if round(x,8)==0:
            print('-'*(h+1),'*','-'*(80-h+1),sep='')
        else:
            if y>0:
                print(' '*(l+1)+'|'+' '*(h-l)+'*',sep='')
            else:
                print(' '*(h)+'*'+' '*(l-h)+'|',sep='')
        x=x+s
else:
    while x<=xk:
        y=exp(x)+exp(-15*x)-4
        h=round(abs(((y-ymin)/(ymax-ymin)))*80)
        if round(x,8)==0:
            print('-'*(h+1),'*','-'*(80-h+1),sep='')
        else:
            print('|'+' '*h+'*',sep='')
        x=x+s       
