"""
[1,2,3,4]
 l     r
use left and right pointer
    l <- track small values
    r <- track big values
    
sum both pointer values to get a guess
if the value is bigger than the target
    it means that we need to decrease our guess value
    decrease right value, the one tha track big values
else if the value is smaller than the target
    it means that we need to increse our guesse value
    increase the left point the one which track small values
oterwhise we found the both pointers that we could summed to get the target
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            guess = numbers[l] + numbers[r]

            if guess > target:
                r -= 1
            elif guess < target:
                l += 1
            else:
                return [l + 1, r + 1]
        
        return [-1,-1]