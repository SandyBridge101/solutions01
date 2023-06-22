from math import sqrt
N=int(input())

arr=list(map(int,input().split()))

arr.sort(reverse=True)

for i in arr:
    if sqrt(i).is_integer():
        continue
    else:
        print(i)
        break