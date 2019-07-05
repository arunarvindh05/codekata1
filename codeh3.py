flag=0
n=int(input())
asd=[]
lst=list(map(int,input().split()))
for i in range(0,n):
  if(lst[i]==i):
    ele=lst[i]
    flag=1
    asd.append(ele)
  asd=sorted(asd)
print(*asd)
if(flag==0):
  print("-1")  
