#using lamda and sort params

nums=[1,2,0,0,0]
# nums=nums.sort(key=lambda x:x==0)



#solution 2

l=0

for r in range(len(nums)):
    if nums[r] !=0:
        nums[r],nums[l]=nums[l],nums[r]
        l+=1
print(nums) 