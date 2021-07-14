# function
def rank(st):
    s = [c for c in st]
    result = 1
    n = len(s)
    fac = 1
    i = n - 2
    while i > -1:
        t = 0
        m = 1
        check = [True for i in range(n)]
        for j in range(i,n):
            if s[j] < s[i]:
                t += 1
            kol = 1
            num = 1
            if check[j]:
                for k in range(j+1,n):
                    if s[k] == s[j] and check[k]:
                        kol += 1
                        num *= kol
                        check[k] = False
                check[j] = False
                m *= num
        fac *= (n - i - 1)
        result += (t * fac) // m
        i -= 1
    return result
#program
fi = open('input.txt','r')
fo = open('output.txt','w')
ok = True
while ok:
    st = fi.readline().strip()
    if st == '#':
        ok = False
    else:
        result = str(rank(st))
        fo.write(result+' \n')
fi.close()
fo.close()
