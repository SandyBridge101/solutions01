N=int(input())

words=[input() for i in range(0,N)]


for i in words:
    print(f'{i[0]}{i[1]}... {i}?')