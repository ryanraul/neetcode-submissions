

"""

[3,4,5,6,1,2]
       l t r
         m

m > l
we are in the left side
our target is between l and m?

[4,5,1,2,3]
 l t m   r
 l r
 m
 t
m < l
we are in the right side
our target is between m and r?

if nums[m] == target:
    return m

if nums[m] >= nums[l]:
    if target > nums[m] or target < nums[l]:
        l = m + 1
    else:
        r = m - 1
elif nums[m] < nums[l]:
    if target < nums[m] or target > nums[r]:
        r = m - 1
    else:
        l = m +1
        


"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:  
        l = 0
        r = len(nums) - 1
        res = -1
        while l <= r:
            m = (l+r)//2

            if nums[m] == target:
                res = m
                break
            
            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        
        return res

        