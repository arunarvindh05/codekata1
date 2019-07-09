asd=int(input())
t=[]
for i in range(0,asd):
    l=list(map(int,input().split()))
    for j in l:
        t.append(j)
print(*sorted(t),end="")
