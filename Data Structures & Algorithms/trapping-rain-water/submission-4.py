"""
using two pointers

[0,2,0,3,1,0,1,3,2,1]
           l   r
it 1: max_left: 0 | max_right: 1 | move left -> trap_water += max(0 - 2, 0) = 0
it 2: max_left: 2 | max_right: 1 | move right -> trap_water += max(1 - 2, 0) = 0
it 3: max_left: 2 | max_right: 2 | move left -> trap_water += max(2 - 0, 0) = 2
it 4: max_left: 2 | max_right: 2 | move left -> trap_water += max(2 - 3, 0) = 0
it 5: max_left: 3 | max_right: 2 | move right -> trap_water += max(2 - 3, 0) = 0
it 5: max_left: 3 | max_right: 3 | move left -> trap_water += max(3 - 1, 0) = 4
it 6: max_left: 3 | max_right: 3 | move left -> trap_water += max(3 - 0, 0) = 7

 - keep the pointer in the highest bar
 - always calculate the highest bar of both sides (left and right)
 - move the side with the smaller bar
    - calculate based on the biggest bar of this side
    - current_position = height[pointer_moved]
    - trapWater += max(biggest_bar_pointer_moved - current_position, 0)

"""
class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_left = 0
        max_right = 0
        trap_water = 0

        while l < r:
            max_left = max(height[l], max_left)
            max_right = max(height[r], max_right)

            if max_left <= max_right:
                l+=1
                trap_water += max(max_left - height[l], 0)
            else:
                r-=1
                trap_water += max(max_right - height[r], 0)
        
        return trap_water




        