def find_indices(n, m, group_a, group_b):
    indices = []
    
    for word in group_b:
        if word in group_a:
            print(*[i+1 for i, x in enumerate(group_a) if x == word])
        else:
            print(-1)
    
    return indices

entry=input().split()
n=int(entry[0])
m=int(entry[1])

ga=[]
gb=[]

for i in range(0,n):
    ga.append(input())
    
for i in range(0,m):
    gb.append(input())


output=find_indices(n, m, ga, gb)