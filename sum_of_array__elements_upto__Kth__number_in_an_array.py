n=int(input())
l=list(map(int,input().split()))
a=int(input())
y=0
for i in l:
    if i<=a:
        y+=i
print(y)