nums = [9,6,4,2,3,5,7,0,1]

N=len(nums)
for n in range(0,N):
    if n not in nums:
        print(n)