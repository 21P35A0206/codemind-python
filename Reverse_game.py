n=int(input())
l=list(map(int,input().split()))
y=[]
for i in l:
    rev=0
    while i>0:
        r=i%10
        rev=rev*10+r
        i=i//10
    y.append(rev)
print(*y)
    