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
print(a)
maxx=minn=a[0]
for i in range(n):
    if a[i]>maxx:
        maxx=a[i]
    if a[i]<minn:
        minn=a[i]
i=0
while i<len(a):
    if round(a[i]-minn,8)==0:
        a+=[0]
        j=len(a)-1
        while j>i:
            a[j]=a[j-1]
            j=j-1
        a[i+1]=maxx
    i+=1
print(a)
