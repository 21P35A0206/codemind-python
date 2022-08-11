n=int(input())
a,b=0,1
l=[0,1]
for i in range(2,n):
    c=a+b
    y=c
    l.append(y)
    a=b
    b=c
print(n in l)