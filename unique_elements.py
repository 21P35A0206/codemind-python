n=int(input())
l=list(map(int,input().split()))
y=[]
for i in l:
    if i not in y:
        y.append(i)
print(*y)
    