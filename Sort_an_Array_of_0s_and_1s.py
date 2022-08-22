n=int(input())
l=list(map(int,input().split()))
s=[]
y=[]
for i in l:
    if i==0:
        s.append(i)
    else:
        y.append(i)
k=s+y
print(*k)