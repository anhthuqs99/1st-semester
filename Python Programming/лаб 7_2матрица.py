'''Переписать все отрицательные элементы матрицы X(10,8) в массив D без пропусков
упорядочит их в массиве D по убыванию. Если в матрице нет ни одного отрицательного
элемента, то напечатать соответствующей текст.
Напечатать исходную матрицу в виде матрицов и сформированный вектор D'''
#Нгуен Ань Тхы
#input
st='+-.0123456789'
stt='0123456789'
okn=True
while okn:
    print('input n,m:')
    nn,mm=map(str,input().split())
    okn=False
    for ch in nn:
        if stt.count(ch)<1:
            okn=True
    for ch in mm:
        if stt.count(ch)<1:
            okn=True
    if not okn:
        n=int(nn)
        m=int(mm)
        if n<1 or n>10 or m<1 or m>8:
            okn=True
    if okn:
        print('input error')
ok=True
while ok:
    H=[]
    print('input matrix D:')
    ok=False
    for i in range(n):
        a=[]
        x=list(map(str,input().split()))
        if len(x)!=m:
            ok=True
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
        H.append(a)
    if ok: print('input error')
#program
D=[]
for p in H:
    for q in p:
        if q<0:
            D.append(q)
l=len(D)
for i in range(l):
    for j in range(i,l):
        if D[i]<D[j]:
            D[i],D[j]=D[j],D[i]
#output
print('исходная матрица:')
for i in range(n):
    print('[',end='')
    for j in range(m):
        print('{:^7}'.format(H[i][j]),end='')
    print(']')
if len(D)<1:
    print('матрице нет ни одного отрицательного элемента')
else:
    print('вектор D:')
    print(D)
