def shift_zeros(nums):
    new=[i for i in nums]
    for i in new:
        if i==0:
            nums.remove(i)
            nums.append(i)

    print(nums)
    
nums = [0,1]

for i in range(0, len(nums)-1):
    if nums[i]==nums[i+1]:
        nums[i]=nums[i]*2
        nums[i+1]=0
        
shift_zeros(nums)

print(nums)