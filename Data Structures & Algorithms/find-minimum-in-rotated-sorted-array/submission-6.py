"""
could use binary search
    - detect if middle of each interaction is sorted

 0 1 2 3 4 5
[3,4,5,6,1,2]
       l m r

- if left value is smaller than right
    - its sorted correctly
        - response could be the most left value (necessary check by the iterations)

- if right value is smaller than middle
    - left = middle + 1
- otherwise
    - save the minimum value between current response and middle value
    - right = middle - 1
 0 1
[2,1]
 l r
 m
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[l]

        while l <= r:
            if nums[l] <= nums[r]:
                res = min(nums[l], res)
                return res
            
            mid = (l+r) // 2

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                res = min(res, nums[mid])
                r = mid - 1
        
        return res