''' Дан одномерный массив. Сформировать новый массив, в который записать
количество чисел, кратных натуральным числам.
B[0]=колочество чисел, кратных 2
B[1]=колочество чисел, кратных 3 и т.д.
Если количество равно нулю, оно в массив не записывается
'''
#Нгуен Ань Тхы
#input
ok=True
while ok:
    print('input a:')
    x=list(map(str,input().split()))
    ok=False
    a=[]
    for c in x:
        if c.startswith('-'):
            ch=c[1:]
        else: ch=c
        if not ch.isdigit():
            ok=True
        else:
            a.append(int(c))
    if ok:
        print('input error')
n=len(a)
#program
m=-1
b=[]
l=0
for i in range(n):
    l=max(l,a[i])
l+=1
for j in range(2,l):
    k=0
    for i in range(n):
        if a[i]%j==0:
            k+=1
    if k>0:
        m+=1
        b.append(k)
        print('количество чисел, кратных',j,': B[',m,']=',b[m])
if len(b)<1:
    print('пустой массив')
