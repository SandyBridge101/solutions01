nums = [0,1,0,3,12]
new=[i for i in nums]
for i in new:
    if i==0:
        nums.remove(i)
        nums.append(i)

print(nums)