n,m=map(int,input().split())
y=[]
s=[]
v=[]
for i in range(1,n+1):
    if n%i==0:
        y.append(i)
for i in range(1,m+1):
    if m%i==0:
        s.append(i)
for i in y:
    for j in s:
        if i==j:
            v.append(i)
print(max(v))
            
        