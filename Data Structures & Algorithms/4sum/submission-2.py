"""
recursive function to check 
the values to sum

stop conditional
k == 2
use two pointers approach


k, start, target
[1,-1,1,-1,1,-1]
[-1,-1,-1,1,1,1]
  a       b c d 
  6 - 3
for i in range(start, len(nums) - k + 1)



"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        res = []
        quad = []
        def kSum(k, start, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    
                    quad.append(nums[i])
                    kSum(k-1, i+1, target - nums[i])
                    quad.pop()
                return
            
            l = start
            r = len(nums) - 1
            while l < r:
                two_sum = nums[l] + nums[r]
                if two_sum == target:
                    res.append(quad + [nums[l], nums[r]])
                    l+=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                elif two_sum > target:
                    r -= 1
                else:
                    l +=1
        
        kSum(4, 0, target)
        return res
                
            
            
        