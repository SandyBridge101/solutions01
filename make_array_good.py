N=int(input())
for _ in range(0,N):
    n=int(input())
    s=list(map(int,input().split()))
    #print(s)
    arr=[[s[i],i] for i in range(len(s))]
    arr.sort()

    print(n-1)
    for i in range(1,n):
        x=arr[i-1][0]-(arr[i][0]%arr[i-1][0])
        arr[i][0]+=x
        print(arr[i][1]+1,x)