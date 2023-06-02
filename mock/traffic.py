def minimum_crossing_time(s, current_color):
    n = len(s)
    time = 1  
    
    while s[(time - 1) % n] != current_color or s[time % n] != 'g':
        time += 1

    return time

N=int(input())

for i in range(0,N):
    s=int(input())
    c=input()