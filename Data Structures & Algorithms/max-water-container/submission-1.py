"""
bars with different sizes
original: [1,7,2,5,4,7,3,6]
what is the maxArea that we could calculate with these bars

[1,7,2,5,4,7,3,6]
maxArea = minHeight between left and right * quantity of bars between left and right
minHeight = min(heights[left], heights[right])
distance = abs(0 - 7) = 7 
distance = abs(1 - 7) = 6
distance = abs(1 - 6) = 5
while(left < right):
    maxArea = maxArea < minHeight * distance ? minHeight * distance : maxArea

    if minHeight == heights[left]:
        left+=1
    else:
        right=-1

[1,7,2,5,4,7,3,6]
   *       ^
 maxAreaCurrent = 7 * 4 = 28
 maxArea = 36
 minHeight = right -> right-=1

"""
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0
        while(left < right):
            distance = abs(left - right)
            minHeight = min(heights[left], heights[right])
            currentArea = minHeight * distance
            if currentArea > maxArea:
                maxArea = currentArea
            
            if heights[left] == minHeight:
                left+=1
            else:
                right-=1
        
        return maxArea




