
def hash_number(string):
    hash_count = 0

    for char in string:
        if char == '#':
            hash_count += 1
    return hash_count
# Create an empty 2D array of size 8x8
array_2d = [['' for _ in range(8)] for _ in range(8)]

# Collect string inputs for each element in the 2D array
for i in range(8):
    user_input = input().split()
    array_2d[i] = user_input

# Print the 2D array
for i in range(1,len(array_2d)-1):
    if hash_number(array_2d[i-1][0])==2 and hash_number(array_2d[i+1][0])==2:
        if hash_number(array_2d[i][0])==1:
            print(array_2d[i],hash_number(array_2d[i][0]))
            print(i,)