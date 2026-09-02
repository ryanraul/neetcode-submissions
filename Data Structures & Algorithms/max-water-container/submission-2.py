"""
using two pointers
[0,1,2,3,4,5,6,7]
[1,7,2,5,4,7,3,6]
   l       r
- keep a pointer in the biggest bar
    if heights[l] <= heights[r]:
        l += 1
    else
        r -= 1
- move other pointer
- always calculte the volume of water based on the smaller pointer bar
    - currentVol = min(heights[l], heights[r]) * r-l
    - keep the biggest volume max(maximum, currentVol)

"""
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maximum = 0
        while l < r:
            currentVol = min(heights[l], heights[r]) * (r-l)
            maximum = max(maximum, currentVol)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -=1

        return maximum

