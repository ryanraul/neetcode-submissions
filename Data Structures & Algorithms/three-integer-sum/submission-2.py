"""
two pointers

sort the array nums
iterate through the array
a = nums[i]

if a > 0:
    break
avoiding repeated values
if i > 0 and a == nums[i - 1]:
    continue

- left = i + 1
- right = len(nums) - 1
while left is less than right:
    b = nums[left]
    c = nums[right]
    three_sum = a + b + c
    if three_sum is equal to the target:
        sum.append([a, b, c])
        move the pointers
            left += 1
            right -=1
        
        avoid repeateds
        while current left pointer value is equals to previous left pointer value
            and left is less than right --> increment left
    else if three_sum < target:
        left += 1
    else 
        right -=1

a + b + c == 0



"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sums = []
        for i, a in enumerate(nums):
            if a > 0:
                break
            
            if i > 0 and a == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1

            while(left < right):
                b = nums[left]
                c = nums[right]
                three_sum = a + b + c

                if three_sum == 0:
                    sums.append([a,b,c])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left+=1
                elif three_sum < 0:
                    left+=1
                else: 
                    right-=1
            
        return sums





















        