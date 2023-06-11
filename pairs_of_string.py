def ismatch(word1,word2):
    for x in word1:
        if x not in word2:
            return False
    for x in word2:
        if x not in word1:
            return False
    return True

words = ["aba","aabb","abcd","bac","aabc"]
s=1
count=0
for w in range(0,len(words)):
    for x in range(w+1,len(words)):
        if ismatch(words[x],words[w])==True:
            #print(w,x)
            count+=1
    s+=1