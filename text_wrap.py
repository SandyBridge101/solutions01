def wrap(string, max_width):
    output=''
    for i in range(1,len(string)+1):
        if i%(max_width)==0:
            output=output+string[i-1]+'\n'
        else:
            output=output+string[i-1]
    return output

print(wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ',4))