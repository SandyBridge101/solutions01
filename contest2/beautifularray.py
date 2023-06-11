s=int(input())
array=list(map(int,input().split()))
lt=[]
gt=[]
eq=[]
for x in array:
    if x<0:
        lt.append(x)
    elif x==0:
        eq.append(x)
    elif x>0:
        gt.append(x)
print(len(lt),' '.join(map(str, lt)))
print(len(gt),' '.join(map(str, gt)))
print(len(eq),' '.join(map(str, eq)))


