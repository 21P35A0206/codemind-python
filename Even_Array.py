n=int(input())
l=list(map(int,input().split()))
y=[]
for i in l:
    if i%2==0:
        y.append(i)
if len(l)==len(y):
    print('True')
else:
    print('False')