n,k=map(int,input().split())
qwe=[]
asd=[]
for i in range(n):
    l=[int(s) for s in input().split()]
    qwe.append(l)
    if 0 in l:
        m=l.index(0)
        asd.append(m)
for i in range(len(qwe)):
    if 0 in qwe[i]:
        for j in range(k):
            qwe[i][j]=0
for i in asd:
    for j in range(n):
        qwe[j][i]=0
for i in qwe:
    print(*i)
