def zipp(word):
    N=len(word)
    
    w=[i for i in range(0,word)]

words = ["bella","label","roller"]
results=[]
sample=words[0]
words=[list(i) for i in words]
#print(words)
for i in sample:
    #print(i)
    count=0
    for x in words:
        if i in x:
            #print(x)
            x.remove(i)
            count+=1
    if count==len(words):results.append(str(i))
    
print(results)