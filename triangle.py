nums = [1,2,1,10]

nums.sort()
print(nums)
max_p=0
for i in range(0,len(nums)-2):
    a=nums[i]
    b=nums[i+1]
    c=nums[i+2]
    
    if a+b>c:
        max_p=max(max_p,a+b+c)
        
print(max_p)