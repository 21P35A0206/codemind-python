n=int(input())
l=list(map(int,input().split()))
a=int(input())
c=0
for i in l:
    fc=0
    if i<=1:
        continue
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            fc+=1
    if fc<1:
        if i>=a:
            c+=1
print(c)