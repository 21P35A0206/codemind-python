n=int(input())
l=list(map(int,input().split()))
s=0
y=0
for i in range(n):
    if i%2==0:
        s=s+l[i]
    else:
        y=y+l[i]
print(abs(s-y))