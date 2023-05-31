import re
N = int(input())
commands=[]
list=[]

def execute(command,argument1,argument2):
    if command=='insert':
        list.insert(int(argument1),int(argument2))
    elif command=='print':
        print(list)
    elif command=='remove':
        list.remove(int(argument1))
    elif command=='append':
        list.append(int(argument1))
    elif command=='sort':
        list.sort()
    elif command=='pop':
        if len(list)>0:
            list.pop()
    elif command=='reverse':
        list.reverse()

x=0

while x<N:
    prompt = input()

    # Define the pattern to match the command and its arguments
    pattern = r'^(\w+)\s+(\d+)(?:\s+(\d+))?$'
    pattern1= r'^\b(\w+)\b$'

    # Use re.match to check if the command matches the pattern
    match = re.match(pattern, prompt)
    match1= re.match(pattern1, prompt)

    if match:
        # Extract the command
        command = match.group(1)
        # Extract the arguments
        argument1 = match.group(2)
        argument2 = match.group(3) if match.group(3) else None

        # Print the results
        execute(command,argument1,argument2)
    else:
        execute(prompt,0,0)
    x=x+1

