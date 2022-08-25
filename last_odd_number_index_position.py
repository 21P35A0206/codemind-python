n=int(input())
l=list(map(int,input().split()))
y=[]
for i in range(n):
    if l[i]%2!=0:
        y.append(i)
print(max(y))
        