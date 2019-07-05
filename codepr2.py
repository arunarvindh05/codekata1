a=int(input())
asd=[]
for i in range(0,a):
  ele=input()
  asd.append(ele)
if not asd: print('')
s1 = min(asd)
s2 = max(asd)
for i, c in enumerate(s1):
  if c != s2[i]:
    print(s1[:i])
  else:  
    print(s1)
