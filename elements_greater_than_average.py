n=int(input())
l=list(map(int,input().split()))
c=0
s=sum(l)//len(l)
for i in l:
    if i>=s:
        c+=1
print(c)