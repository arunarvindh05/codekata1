asd=int(input())
qwe=list(map(int,input().split()))
poi=[]
for i in qwe:
  zxc=bin(i)
  poi.append(zxc)
f=sorted(poi,reverse=True)
for j in f:
  print(int(j,2))
