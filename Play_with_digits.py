n=int(input())
l=list(map(int,input().split()))
y=0
for i in l:
    while i>0:
        r=i%10
        y=y+r
        i=i//10
print(y)
