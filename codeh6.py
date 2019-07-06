flag=0
n=int(input())
lst=list(map(int,input().split()))[:n]
asd=[]
for i in range(0,n):
  if(lst.count(lst[i])>1):
    c=lst[i]
    flag=1
    break
print(c)
if(flag==0):
  print("unique")
