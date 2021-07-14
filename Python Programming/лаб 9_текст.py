menu='''
1. Выравнивание по ширине.
2. Выравнивание по левому краю.
3. Выравнивание по правому краю.
4. Замена во всем тексте одного слова другим.
5. Удаление заданого слова из текста.
6. Замену арифметических выражений, состоящих из умножения и деления,на результат их вычисления.
7. Найти найболее часто встречающееся слово в каждом предложении.'''
#
st='''I want to tell you even
though to. The sad times have already past. Close
your eyes and feel my moved heart. My gaze at you
Do not wait for a special miracle. There is a
roug road in front of
us. With unknowable future and obstacles I
will not change. I can not give up. Protect me with
an unchanged love. Also my wounded heart. Looking
in your eyes no words are needed. Time
has stopped. I love you just like this. The 
longed end of wandering. I leave behind This
world. Unending sadness. In the many unknowable
paths. I follow a dim light. It is something we
will do together to the end 0 / 0. Into
my new world. 4 4x 4 / 6 + 9 * -10 * 9 / 30 fine.
'''
#make string S
def makeS():
    S=[]
    s=''
    for c in st.split():
        s+=c+' '
        if c.endswith('.'):
            S.append(s[:len(s)-2])
            s=''
    if s!='':
        S.append(s)
    return(S)
#Выравнивание
def choise(k,S):
    for i in range(len(S)):
        s=S[i]
        while s.startswith(' '):
            s=s.replace(' ','',1)
        while s.find('  ')>0:
            s=s.replace('  ',' ')
        S[i]=s
    maxx=0
    for i in range(len(S)):
        maxx=max(maxx,len(S[i]))
    if k==1:
        for i in range(len(S)):
            s=S[i]
            d=s.count(' ')-1
            if d>0:
                l=(maxx+1-(len(s)-d))//d
                l1=(maxx+1-(len(s)-d))%d
            else:
                l=(maxx+1-(len(s)-d))
                l1=0
            s=s.replace(' ',' '*l,d)
            s=s.replace(' '*l,' '*(l+1),l1)
            S[i]=s
    elif k==3:
        for i in range(len(S)):
            S[i]=S[i].rjust(maxx)
    return(S)
#Замена во всем тексте одного слова другим
def choise4(s1,s2):
    s1=s1.upper()
    for i in range(len(S)):
        a=[c for c in S[i].split()]
        for j in range(len(a)):
            if a[j].upper()==s1:
                a[j]=s2
            elif a[j].upper()==s1+'.':
                a[j]=s2+'.'
        ss=''
        for j in range(len(a)):
            if a[j]!='':
               ss+=a[j]+' '
        S[i]=ss[:len(ss)-1]
    return(S)
#Замену арифметических выражений, состоящих из умножения и деления,на результат их вычисления
def choise6():
    for j in range(len(S)):
        a=[c for c in S[j].split()]
        i=1
        while i<len(a):
            if a[i] in ['*','/']:
                try:
                    x=float(a[i-1])
                    y=float(a[i+1])
                    if a[i]=='*':
                        z=x*y
                    else:
                        z=x/y
                    a[i-1]=str(z)
                    a.pop(i)
                    a.pop(i)
                except:
                    i+=1
            else:
                i+=1
        ss=''
        for c in a:
            ss+=c+' '
        S[j]=ss[:len(ss)-1]
    return(S)
#Найти найболее часто встречающееся слово в каждом предложении
def choise7():
    a=[]
    index=0
    for s in S:
        for c in s.split():
            if c.endswith('.'):
                a.append(c[:len(c)-1].upper())
                index+=1
                maxx=0
                ch=''
                for v in a:
                    if v.isalpha() and a.count(v)>maxx:
                        maxx=a.count(v)
                        ch=v
                if maxx>0:
                    print('найболее часто встречающееся слово в',index,' предложении:',ch)
                a=[]
            else:
                a.append(c.upper())
    print()
def printS():
    for s in S:
        print(s)
l=2
# S=makeS()
S = st.split('\n')
ok=True
while ok:
    try:
        print('Menu:',menu)
        k=int(input('Input your choise: '))
        if k>0 and k<4:
            l=k
            S=choise(l,S)
            printS()
        elif k==4:
            s1=str(input('Input the word you need to change: '))
            s2=str(input('Input the word will replace this word: '))
            choise4(s1,s2)
            S=choise(l,S)
            printS()
        elif k==5:
            s1=str(input('Input the word you want to delete: '))
            choise4(s1,'')
            S=choise(l,S)
            printS()
        elif k==6:
            S=choise6()
            S=choise(l,S)
            printS()
        elif k==7:
            choise7()
    except:
        ok=False
    if k<1 or k>7:
        ok=False
    if not ok:
        print('Finish')
