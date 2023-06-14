def index_difference(string):
    index_list=[]
    index=0
 
    for char in string:
        if char == '#':
            index_list.append(index)
        index+=1
    index_list.append(0)
        
    try:
        return (index_list[1]-index_list[0])-1
    except:
        return 0


string='#...#...'

print(index_difference(string))

