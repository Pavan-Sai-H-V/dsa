class Solution(object):
    def twoSum(self, nums, target):
        l,r=0,len(nums)-1
        sum=0
        nums = sorted([(num, i) for i, num in enumerate(nums)])
        while l<r:
            sum=nums[l][0]+nums[r][0] # we use number from list like [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)] -here its (i,num)
            if sum==target:
                return (nums[l][1],nums[r][1])
            elif sum < target:
                l +=1
            else:
                r -=1

                
#nums=[1,2,3,4,5]
# # for i,v in enumerate(nums):
# #     print(i,v)

# nums_index = sorted([(num, i) for i, num in enumerate(nums)])
# print(nums_index)