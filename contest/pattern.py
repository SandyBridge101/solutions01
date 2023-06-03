N=int(input())

input=[input() for i in range(0,N)]
words=[]
for w in input:
    w={char: index for index, char in enumerate(w)}
    words.append(w)
print(words)
sign='?'
intersection=words[0]


for m,key in range(0,len(words)):
    intersection=intersection & words[m][key]

print(intersection)