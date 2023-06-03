def get_index(str,c):
    return [i for i, x in enumerate(str) if x == c]

def find_max_time(index,s):
    max_time=0
    for x in index:
        count=0
        for x in range(x,len(s)):
            if s[x]=='g':
                break
            else:
                count+=1
        if count>max_time:
            max_time=count

    return max_time

N=int(input())
times=[]
for cases in range(0,N):
    entry=input().split()
    s=input()

    s=s+s

    length=entry[0]
    current=entry[1]


    index=get_index(s,current)


    times.append(find_max_time(index,s))
    
for t in times:
    print(t)