n=int(input())
l=list(map(int,input().split()))
a=[abs(i) for i in l]
y=[]
for i in a:
    if i==0:
        print(1,end=' ')
    else:
        c=0
        while i>0:
            r=i%10
            c+=1
            i=i//10
        print(c,end=' ')