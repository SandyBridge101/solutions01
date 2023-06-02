N=int(input())

def unique(array):
    unique=[]
    i=0
    for i in array:
        if i not in unique:
            unique.append(i)
        else:
            return False
        
    return True
        


members=input().split()
bad=input().split()
count=0
for m in members:
    if m not in bad:
        if unique(m):
            count=count+1

print(count)
