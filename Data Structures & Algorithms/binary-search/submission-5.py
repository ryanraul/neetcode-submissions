"""

- set two pointers
    - left: indicates the beginning of the collection
    - right: indicates the end

- for each iteration 
    - calculates the middle pointer of this list
    - mid = (left + right) // 2
    
    - if the mid value is equal to the target 
        - yes: return mid

    - check if the target is greater than the mid value
        - yes: we can stop to looking for the left side of the list
            - l = mid + 1
    - oterwhise:
        - its not necessary looking for the target on the right side

- in case we cannot find the target value return -1

target=9
       0 1 2 3 4 5
nums=[-1,0,3,5,9,12]
             l m  r

       5 // 2 = 2
       nums[2] = 3
       3 < 9 => l = mid + 1 = 3

       4 + 5 = 9 // 2 = 4


"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l+r) // 2
            print(mid)
            if nums[mid] == target:
                return mid
            
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return -1