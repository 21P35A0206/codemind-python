n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    y=i
    c=0
    while i>0:
        r=i%10
        c=c*10+r
        i=i//10
    if y==c:
        s+=1
print(s)