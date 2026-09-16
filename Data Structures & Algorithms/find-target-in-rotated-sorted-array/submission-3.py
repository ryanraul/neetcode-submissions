"""
 0 1 2 3 4 5 -> target = 1
[2,3,4,5,6,1]
           r
           l

 0 1 2 3 4 5
[3,5,6,0,1,2]
 l     m   r


 0 1 2 3 4 5
[1,2,3,4,5,6]
       l
       r

 if nums[mid] == target:
    return mid

 if nums[mid] > target >= nums[l]:
    r = mid - 1
 oterwhise
    l = mid + 1
 0 1 2


[5,1,3]
 l m r

 

"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1

        while l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1