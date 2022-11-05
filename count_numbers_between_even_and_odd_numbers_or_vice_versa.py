n=int(input())
l=list(map(int,input().split()))
a=0
d=0
for i in range(1,n-1):
    if(i-1)%2!=0 and l[i+1]%2!=0 and i!=0:
        a=a+1
    if(i-1)%2==0 and l[i+1]%2!=0 and i!=0:
        d=d+1
print(a+d)