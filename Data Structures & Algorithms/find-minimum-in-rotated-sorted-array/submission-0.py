"""
[4,5,0,1,2,3]
 l         r
how do i know this was rotated?
r > l? 
    was rotated

mid = 0 + 5 // 2 = 2
nums[mid] < nums[l]:
    res = nums[mid]
    l = mid - 1

[4,5,0,1,2,3]
 r l

mid 0 + 1 // 2
0

nums[mid] < nums[l]:
elif nums[mid] > nums[l]:

Not rotated cenario
l = 0
r = len(nums) - 1

if nums[r] > nums[l]
    return nums[l]

[3,4,5,6,1,2]
         l r
res = nums[r]

while l <= r:
    mid = (l+r) // 2

    if nums[mid] < res:
        res = nums[mid]:
        r = mid - 1
    else
        l = mid + 1


"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        if nums[r] > nums[l]:
            return nums[l]
        
        res = nums[r]

        while l <= r:
            mid = (l+r)//2

            if nums[mid] < res:
                res = nums[mid]
                r = mid - 1
            else:
                l = mid + 1
        
        return res

        