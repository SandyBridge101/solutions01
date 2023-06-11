def isgood(i,j,nums):
    if nums[i]==nums[j] and i<j:
        return True
    
nums = [1,2,3,1,1,3]

s=1
count=0
for w in range(0,len(nums)):
    for x in range(w+1,len(nums)):
        if isgood(w,x,nums)==True:
            print(w,x)
            count+=1