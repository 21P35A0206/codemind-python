n=int(input())
m=int(input())
y=[]
s=[]
for i in range(1,n):
    if n%i==0:
        y.append(i)
for j in range(1,m):
    if m%j==0:
        s.append(j)
if sum(y)==m and sum(s)==n:
    print('Amicable')
else:
    print('Not Amicable')
    
        
        