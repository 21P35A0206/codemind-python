n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(n-2):
    if l[i]%2!=0:
        if l[(i+1)]%2!=0:
            if l[(i+2)]%2!=0:
                s+=1
print(s)