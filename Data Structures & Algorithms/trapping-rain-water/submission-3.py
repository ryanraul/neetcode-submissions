"""
[0,2,0,3,1,0,1,3,2,1]
 l                 r
 which one is smaller?
 l 
 decrement left
[0,2,0,3,1,0,1,3,2,1]
             l r
0,1 -> 0
0-2 = 0
(2,1) -> 1
1-2 = 0
2,2 -> 2l
2-0 = 2
2,2 -> 2l
2-3 =0 0
3,2 -> 2r
2-3 =0
3,3 -> 3l
3-1 = 2 +2 = 4
vol = 4
3,3 -> 3l
3-0 = 3 + 4 = 7
vol = 7
3,3 -> 3l
3-1 = 2 + 7 = 9

save the bigger height between the two pointers (left and right)
always move the smaller height side (left or right)
and calculate the volume using the previous height minus current height
 -> left+=1
 -> heigh[left-1] - height[left]
 or
 -> right -= 1
 -> height[right+1] - height[right]
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        volume_trap = 0
        big_left, big_right = -1,-1

        while left < right:
            big_left = max(big_left, height[left])
            big_right = max(big_right, height[right])

            if big_left <= big_right:
                left+=1
                current_volume = big_left - height[left]
            else:
                right-=1
                current_volume = big_right - height[right]

            volume_trap += max(current_volume,0)
        return volume_trap

        