grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]
grid_rows=len(grid)
grid_cols=len(grid[0])
hourglass_sum=0
for row in range(1,grid_rows-1):
    for col in range(1,grid_cols-1):
        nsum=0
        nsum=nsum+grid[row][col]+grid[row-1][col-1]+grid[row+1][col-1]+grid[row-1][col+1]+grid[row+1][col+1]+grid[row+1][col]+grid[row-1][col]
        hourglass_sum=max(nsum,hourglass_sum)
print(hourglass_sum)