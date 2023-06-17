N=int(input())

for _ in range(N):
    n=int(input())
    s=list(map(int,input().split()))
    b=[0]*n
    b[-1]=s[-1]
    b[0]=s[0]
    for i in range(1,n-1):
        b[i]=min(s[i-1],s[i])
    print(*b)