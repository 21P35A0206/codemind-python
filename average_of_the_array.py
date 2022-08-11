n=int(input())
l=list(map(int,input().split()))
s=sum(l)/len(l)
print('{:.2f}'.format(s))