n=int(input())
lst=list(map(int,input().split()))[:n]
asd=[]
for i in range(0,n):
  if(lst.count(lst[i])>1):
    c=lst[i]
    asd.append(c)
  sorted(asd)
  
asd = list(dict.fromkeys(asd))
print(*asd)
