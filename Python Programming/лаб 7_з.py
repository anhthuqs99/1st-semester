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
    else:
        print('input error, n out of range')
ok=True
#program
a=[]
for i in range(n):
    a.append([])
    for j in range(n):
        a[i].append(0)
k=0
for i in range(n-1):
    for j in range(i+1,n):
        a[j][i]=n*n-k
        a[i][j]=pow(2,k)
        k+=1
for q in a:
    print('[',end='')
    for p in q:
        print('{:^10}'.format(p),end='')
    print(']')

