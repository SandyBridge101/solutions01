s="abcd"
t="beadjjcka"

len_t=len(t)
ls=[str(i) for i in s]
lt=[str(i) for i in t]
ls.sort()
lt.sort()
print(ls)
print(lt)
#print(''.join(c for c in t))
output=[]

for letter in lt:
    #print(f'@{letter}')
    if letter in ls:
        ls.remove(letter)
    else:
        output.append(letter)
        print(letter)

print(''.join(i for i in output))