sup=set(input().split())
N=int(input())
sub=[set(input().split()) for i in range(0,N)]

output=False
for s in sub:
    if sup.intersection(s)!=s:
        output=False
        break
    else:
        output=True