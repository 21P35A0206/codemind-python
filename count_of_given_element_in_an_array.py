n=int(input())
l=list(map(int,input().split()))
z=int(input())
count=0
for i in l:
    if i==z:
        count=count+1
print(count)
        
