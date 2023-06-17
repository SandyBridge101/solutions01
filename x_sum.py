N=int(input())

for _ in range(N):
    dimension=list(map(int,input().split()))
    row=dimension[0]
    col=dimension[1]
    board=[list(map(int,input().split())) for i in range(0,row)]

    print(board)
    s=0
    while s!=row:
        x=0
        print(f'{s} diagonal')
        for r in range(s,len(board)):
            print(r,x)
            x+=1
        s+=1