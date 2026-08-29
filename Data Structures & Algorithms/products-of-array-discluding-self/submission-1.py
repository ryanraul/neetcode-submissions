"""
numbers [1,2,3,4]
prefix  [1,1,2,6]
sufix   [24,12,4,1]
result  [24, 12, 8, 6]


prefix = [] 
suffic = []

prefix[0] = 1
for i in range(len(nums)):
    prefix[i+1] = prefix[i] * nums[i]

suffix = []
suffix[len(nums)-1] = 1
for j in range(len(nums) - 1, 0, -1):
    suffix[j - 1] = suffix[j] * nums[j]

reseponse = []
for i in range(len(nums)):
    response.append(prefix[i] * suffix[i])

return response
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size_numbers = len(nums)
        prefix = [0] * size_numbers
        suffix = [0] * size_numbers

        prefix[0] = 1
        for i in range(size_numbers - 1):
            prefix[i+1] = prefix[i] * nums[i]

        suffix[size_numbers-1] = 1
        for j in range(size_numbers - 1, 0, -1):
            suffix[j - 1] = suffix[j] * nums[j]

        response = []
        for i in range(size_numbers):
            response.append(prefix[i] * suffix[i])

        return response