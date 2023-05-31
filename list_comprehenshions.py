x = 1
y = 1
z = 1
n = 2

r1=[a for a in range(0,x+1)]
r2=[b for b in range(0,y+1)]
r3=[c for c in range(0,z+1)]

ls=[[i,j,k]for i in r1 for j in r2 for k in r3 if i+j+k!=n ]


print(ls)

#numbers = [0, 1]
#letters = [0,1,2]
#pairs = [(num, letter) for num in numbers for letter in letters]
#print(pairs)