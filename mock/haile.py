number=int(input())
students=[]
for i in range(0,number):
    data=input().split('#')
    students.append(data)

for i in students:
    print(i[0],i[1],i[2])