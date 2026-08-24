"""
we can set left and right pointer
and use binary search to find the index
while left <= right
mid = (left+right)//2
if mid value is equal
return the mid as the index
else if mid value > target
left = mid + 1
otherwise 
right = mid
if right == left
    if current_value > target 
        return left+1
    else 
        return left-1
    


"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            mid = (left+right)//2
 
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid
            else:
                left = mid + 1
            
            if left == right:
                return left
        return -1


