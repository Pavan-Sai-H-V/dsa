#given an array nums containg digits of numbers of [0,n] range. find out the missing number the sequence
nums1=[0,1,2,4]
# for i,v in enumerate(nums):
#     print(i,v)


#solution_1

# def sum1(nums):
#     missing_val=[]
#     nums.sort()
#     for i,v in enumerate(nums):
#         if i!=v:
#            missing_val.append(v-1)
#         if v==len(nums)-1:
#            missing_val.append(v+1)
#     return missing_val

#solution_2

# def sum1(nums):
#     nums.sort()
#     for i,v in enumerate(nums):
#         if i!=v:
#           return v-1
#         if v==len(nums)-1:
#           return v+1


#solution_3. best time complexity
def sol2(n):
    t = (sum(range(len(n)+1))- sum(n))
    print(t)

sol2(nums1)