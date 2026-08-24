class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sums = []
        for i, val in enumerate(nums):
            if val > 0:
                return sums
            
            if i > 0 and nums[i] == nums[i-1]: 
                continue

            left = i + 1
            right = len(nums) - 1

            while(left < right):
                result = nums[i] + nums[left] + nums[right]
                if result == 0:
                    sums.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while nums[left] == nums[left - 1] and left < right:
                        left+=1
                elif result < 0:
                    left+=1
                else:
                    right-=1
        return sums