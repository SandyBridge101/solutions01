N = int(input())  # Number of test cases
for _ in range(0,N):
    input()  # Read the empty line before each test case
 
    # Read the chessboard
    chessboard = [input() for _ in range(8)]
 
    # Find the position of the bishop
    #print(chessboard)
    for x in range(1,7):
        for y in range(1,7):
            if chessboard[x][y]=="#" and chessboard[x+1][y+1]=="#" and chessboard[x-1][y-1]=="#" and chessboard[x+1][y-1]=="#" and chessboard[x-1][y+1]=="#":
                print(x+1,y+1)