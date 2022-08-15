n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
y=[]
for i in l:
    if i>=a and i<=b:
        y.append(i)
if len(y)==0:
    print('-1')
else:
    print(sum(y))