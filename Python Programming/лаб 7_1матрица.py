'''в квадратной матрице H(7,7) поменять местами в каждом столбце максимальный элемент
с диагональным. Из преобразованной матрицы получить матрицу D(6,7)будем
вычеркивания элементов главной диагонали. Матрицу D напечатать в виде матрицы.
Сформировать также одномерный массив R из отрицательных элеметов матрицы D'''
#Нгуен Ань Тхы
#input
st='+-.0123456789'
stt='0123456789'
okn=True
while okn:
    print('input n:')
    nn=input()
    okn=False
    for ch in nn:
        if stt.count(ch)<1:
            okn=True
    if not okn:
        n=int(nn)
        if n<1 or n>7:
            okn=True
    if okn:
        print('input error, n out of range')
ok=True
while ok:
    H=[]
    print('input matrix H:')
    ok=False
    for i in range(n):
        a=[]
        x=list(map(str,input().split()))
        if len(x)!=n:
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
print('исходная матрица H:')
for q in H:
    print('[',end='')
    for p in q:
        print('{:^7}'.format(p),end='')
    print(']')
D=[[]*(n-1) for i in range(n)]
R=[]
#program
for j in range(n):
    maxx=H[0][j]
    k=0
    for i in range(n):
        if H[i][j]>maxx:
            maxx=H[i][j]
            k=i
    H[j][j],H[k][j]=H[k][j],H[j][j]
for i in range(n-1):
    D[i].extend(H[i+1][:i+1])
    D[i].extend(H[i][i+1:])
    for q in D[i]:
        if q<0:
            R.append(q)
#output
print('преобразованная матрица H:')
for q in H:
    print('[',end='')
    for p in q:
        print('{:^7}'.format(p),end='')
    print(']')
print('матрица D:')
for i in range(n-1):
    print('[',end='')
    for p in D[i]:
        print('{:^7}'.format(p),end='')
    print(']')
print('Массив R:')
if len(R)>0:
    print(R)
else:
    print('пустой массив')
