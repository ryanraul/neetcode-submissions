"""
use binary search
we know that result is between 0 and x
and that is a range, so we can use binary search between this values
left = 0 
right = 0
while left is less or equal to right
    mid == (left + right) // 2

    if mid**2 is equal to x
        return mid
    else if mid**2 is greater than x
        it means that our result should be smaller
        so update right with mid - 1
    otherwise
        it means that our result should be greater
        so update left with mid + 1
        also save this value, because one of the requirements
            in the question is that the result should be 
            "rounded down" to the nearest integer
            so this current mid is the smaller value approuach of the result
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        res = 0

        while left <= right:
            mid = (left+right)//2

            if mid**2 == x:
                return mid
        
            if x < mid**2:
                right = mid - 1
            else:
                left = mid + 1
                res = mid

        return res

