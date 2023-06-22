N=int(input())
solved=0
for _ in range(N):
    problem=list(map(int,input().split()))
    decision=sum(problem)
    if decision>=2:solved+=1

print(solved)