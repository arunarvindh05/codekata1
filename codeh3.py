
n=int(input())
asd=[]
lst=list(map(int,input().split()))
for i in range(0,n):
  if(lst[i]==i):
    ele=lst[i]
    asd.append(ele)
  asd=sorted(asd)
print(*asd)
  
