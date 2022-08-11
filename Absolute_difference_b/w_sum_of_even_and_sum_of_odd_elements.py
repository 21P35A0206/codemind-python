n=int(input())
l=list(map(int,input().split()))
s=0
y=0
for i in l:
    if i%2!=0:
        s=s+i
for i in l:
    if i%2==0:
        y=y+i
print(abs(s-y))