n=int(input())
l=list(map(int,input().split()))
avg=sum(l)//len(l)
if avg in l:
    print('True')
else:
    print('False')