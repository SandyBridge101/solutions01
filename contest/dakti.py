import re
def get_number(string):
    match = re.search(r'\d+', string)
    if match:
        return int(match.group())
    else:
        return 0


N=int(input())

songs=[input().split() for i in range(0,N)]

#print(songs)

for line in songs:
    output=[]
    out=""
    for word in line:
        order=get_number(word)
        word=word.replace(str(order),'')
        output.append((order,word))
        output.sort()
        
        merged=' '.join(element[1] for element in output)
        
    print(merged)
        


