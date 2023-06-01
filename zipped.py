#entry=input().split()

N=5
X=3

students=[i for i in range(0,N)]

subjects=[]


for i in range(0,X):
    subject=input()
    subjects.append(subject.split())
    


print(students)

print(subjects)



new=list(zip(students,zip(*subjects)))
print(new)
for x in new:
    sum=0
    id=x[0]
    for i in range(0,len(x[1])):
        sum=sum+float(x[1][i])
        
    print(id,sum/len(x[1]))

