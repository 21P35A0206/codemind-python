n=int(input())
l=list(map(int,input().split()))
c=0
s=max(l)
for i in l:
    if len(str(i))==len(str(s)):
        c+=1
print(c)