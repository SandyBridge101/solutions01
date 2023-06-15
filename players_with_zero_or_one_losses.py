from collections import Counter
matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
answer=[[],[]]

winners,losers=zip(*matches)
list(winners)
losers=list(losers)
print(losers)
losers.sort()
ans=[sorted(set(winners)-set(losers)),sorted([i for i,j in Counter(losers).items() if j==1])]
print(ans)
