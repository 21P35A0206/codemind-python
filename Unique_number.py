n=int(input())
y=[]
while n>0:
    r=n%10
    y.append(r)
    n=n//10
s=set(y)
if len(s)==len(y):
    print('Unique Number')
else:
    print('Not Unique Number')