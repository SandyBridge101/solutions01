salary=[10,20,10,20,30,40,20,10,90]

def remove(value,arr):
    for i in range(0,arr):
        if value==arr[i]:
            arr.pop(i)
            
salary.sort()
_max=salary[0]
_min=salary[len(salary)-1]
sum=0
n=0
print(salary,_max,_min)

for i in salary:
    if i!=_max and i!=_min:
        sum=sum+i
        n+=1
        
print(float(sum/n))