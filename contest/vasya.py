N=int(input())

points=input().split()
max_point=int(points[0])
min_point=int(points[0])
count=0
for point in points:
    if int(point)>max_point:
        max_point=int(point)
        #print('max',max_point)
        count+=1
    if int(point)<min_point:
        min_point=int(point)
        #print('min',min_point)
        count+=1
        
print(count)