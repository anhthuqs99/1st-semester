'''
Во введенном массиве вычислить сумму положительных элементов, расположенных на позициях
с четными индексами. Найденную сумму записать вместо третьего отрицательного элемента. Если в массиве нет
трех отрицательных элементов, то вывести об этом сообщение
'''
#Нгуен Ань Тхы
from math import *
#input
ok=True
st='+-.0123456789'
stt='0123456789'
while ok:
    a=[]
    print('input a:')
    x=list(map(str,input().split()))
    ok=False
    for c in x:
        if st.count(c[0])<1:
            ok=True
        else:
            e=0
            d=0
            t=0
            for ch in range(1,len(c)):
                if c[ch]=='e': e+=1
                elif c[ch]=='+'or c[ch]=='-': d+=1
                elif c[ch]=='.': t+=1
                elif stt.count(c[ch])<1: ok=True
                if e>0 and t>0: ok=True
                if e>1 or d>1 or d>e or t>1: ok=True
            if stt.count(c[len(c)-1])<1: ok=True
        if not ok:
            a.append(float(c))
    if ok: print('input error')
n=len(a)
#program
s=0
k=0
j=-1
for i in range(n):
    if a[i]>=0:
        if i%2==0: s+=a[i]
    else:
        k+=1
        if k==3: j=i
if j>0:
    a[j]=s
    print(a)
else:
    print('в массиве нет трех отрицательных элементов')
    print('сумма:',s)
