
stones=input().split()
unique=[]
i=0
for i in stones:
    if i not in unique:
        unique.append(i)

if len(unique)>=5:
    print("YES")
else:
    print("NO")