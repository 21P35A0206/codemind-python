n=int(input())
l=list(map(int,input().split()))
s=0
y=0
for i in range(n):
    if l[i]%2==0:
        if i%2==0:
            s+=1
    if l[i]%2==0:
        y+=1
if s==y:
    print(True)
else:
    print(False)