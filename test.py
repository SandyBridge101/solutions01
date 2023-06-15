matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
answer=[[],[]]

for m in matches:
    count_0=0
    count_1=0
    x=0
    for x in range(0,len(matches)):
        if m[0]==matches[x][1]:
            count_0+=1
        if m[1]==matches[x][1]:
            count_1+=1
    #print(m,count_0,count_1)
    if count_0==0:
        print(m[0])
        answer[0].append(m[0])
    if count_1==1:
        print(m[1])
        answer[1].append(m[1])



ans=[sorted(list(set(answer[0]))),sorted(list(set(answer[1])))]

print(ans)

