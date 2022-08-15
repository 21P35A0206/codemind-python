n=int(input())
l=list(map(int,input().split()))
y=[]
for i in l:
    fc=0
    if i<=1:
        continue
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            fc=fc+1
    if fc<1:
        y.append(i)
avg=sum(y)/len(y)
print('%.2f'%avg)
        