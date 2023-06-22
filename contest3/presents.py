N=int(input())

p=list(map(int,input().split()))

friends=[(i+1,p[i]) for i in range(0,len(p))]

friends.sort(key=lambda x:x[1])
print(*[i[0] for i in friends])

