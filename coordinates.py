x=3
y=4

points = [[2,3]]
valid=[]
least_dist=10000
least_point=[]
for point in points:
    dist=0
    if point[0]!=x and point[1]!=y:
        continue
    else:
        dist=abs(x - point[0]) + abs(y - point[1])
        if dist<least_dist:
            least_dist=dist
            least_point=[[point,points.index(point)]]
        elif dist==least_dist:
            least_point.append([point,points.index(point)])
            #valid.append((point,points.index(point)))
        print(f'manhattan distance {dist} point{point} least distance so far{least_dist}')
        #valid.append((point,points.index(point),dist))
        
least_point.sort(key=lambda x: x[1])

try:
    output=least_point[0][1]
except:
    output=-1
    
print(output)



"""
for point in points:
    dist=0
    if point[0]!=x and point[1]!=y:
        continue
    else:
       
        print(point)
        dist=abs(x - point[0]) + abs(y - point[1])
        print(f'manhattan distance {dist}')
        valid.append((point,points.index(point),dist))
        
print(valid)
"""