n=int(input())


for i in range(0,n):
    rect1=list(map(int,input().split()))

    rect2=list(map(int,input().split()))
    rect1.sort()
    rect2.sort()
    
    if rect1[0] == rect2[0] and rect1[1] + rect2[1] == rect1[0] or rect1[1] == rect2[1] and rect1[0] + rect2[0] == rect1[1]:
        print("Yes")
    else:
        print("No")
        

