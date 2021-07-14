x=float(input('x='))
e=float(input('e='))
w=float(input('шаг печати:'))
t=1
s=0
n=1
print('-'*58)
print('|','{:^12}'.format('№ интерации'),'|','{:^20}'.format('текущий член'),'|','{:^22}'.format('текущее значение суммы'),'|',sep='')
print('-'*58)
while abs(t)>e:
    s=s+t*2
    print('|','{:^12}'.format(n),'|','{:^20.10g}'.format(t),'|','{:^22.10g}'.format(s),'|',sep='')
    print('-'*58)
    n=n+1
    t=pow(x,2*n-1)
