"""

a + b + c

order numbers
we neeed to order the array to help us to void duplicate values

iterate thrugh the array
get the first value of the sum
    if index > 0 and numbers[i - 1] == nubmers[i] -- avoid repeated values
        continue
    
    l = i + 1
    r = len(numbers) - 1

    while l < r:
        guess = nums[i] + nums[l] + nums[r]

        if guess == 0
            save the indexes in the response array
            increase left pointer
            decrease right pinter
            avoid repeated values
            while numbers[l] == numbers[l-1] and l < r:
                l+=1
            
            continue

        if guess > 0:
            r -= 1
        else:
            l += 1

"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        response = []
        nums = sorted(nums)
        print(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            l = i + 1
            r = len(nums) - 1
            while l < r:
                guess = nums[i] + nums[l] + nums[r]

                if guess == 0:
                    response.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while nums[l-1] == nums[l] and l < r:
                        l+=1

                    continue

                if guess > 0:
                    r-=1                
                else:
                    l+=1
                    
        print(response)
        return response
