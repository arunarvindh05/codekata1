qwe=input()
b=0
asd=[]
for i in range(0,len(qwe)-1):
    for j in range(i+1,len(qwe)):
        k=qwe[i:j+1]
        l=k[::-1]
        if k==l:
            asd.append(len(qwe)-len(l))
print(min(asd))
