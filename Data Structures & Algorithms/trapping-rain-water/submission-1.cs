/*
- 

 - [0,2,0,3,1,0,1,3,2,1]
 - [0,0,2,2,3,3,3,3,3,3]- All the max left of current position
 - [3,3,3,3,3,3,3,2,1,0]- All the max right of current postison
 - [0,0,2,0,2,3,2,0,0,0]- Min(maxLeft,maxRight) - currentPosition
 
 - maxLeft = 0
 - maxRight = 1

 -we could use two pointers approach
 - while left < right

 - maxLeft = Math.Max(maxLeft, array[left]);
 - maxRight = Math.Max(maxLeft, array[right]);

 - if maxLeft <= maxRight
    left++;
    res = Math.Max(0, maxLeft - array[left])
 - else
    right --;
    res = Math.Max(0, maxRight - arrayRight)
    
*/
public class Solution {
    public int Trap(int[] height) {
        int maxLeft = 0, maxRight = 0;
        int left = 0, right = height.Length - 1;
        int response = 0;
        while(left < right){
            maxLeft = Math.Max(maxLeft, height[left]);
            maxRight = Math.Max(maxRight, height[right]);

            if(maxLeft <= maxRight){
                left++;
                response += Math.Max(0, maxLeft - height[left]);
            }
            else 
            {
                right--;
                response += Math.Max(0, maxRight - height[right]);
            }
        }

        return response;
    }
}
