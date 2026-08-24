/*
    [0,2,0,3,1,0,1,3,2,1]
    - we could use tow pointers approach
    - left and right
    - left start with 0 and right = left + 1
    - each increment of right update maxRightHeight with the max height found
    - if right height is bigger or equal left height
        - stop increment right
        - minHeight = get the min height between left and right
    - left increment until right and sum each position 
        - calculus: minHeight - height[left]

    [0,2,0,4,1,0,1,3,2,1]

*/
public class Solution {
    public int Trap(int[] height) {
        int left = 0, right = left + 1;
        int maxRightHeightIndex = -1;
        int minHeight = 0;
        int maxVolume = 0;

        while(right < height.Length) {
            maxRightHeightIndex = maxRightHeightIndex != -1 && height[maxRightHeightIndex] > height[right] 
                ? maxRightHeightIndex 
                : right;

            if(height[right] >= height[left] || right == height.Length - 1){
                minHeight = Math.Min(height[left], height[maxRightHeightIndex]);
                while(left < maxRightHeightIndex){
                    var currentVolume = minHeight - height[left];
                    maxVolume += currentVolume < 0 ? 0 : currentVolume;
                    left++;
                }
                maxRightHeightIndex = -1;
                right = left + 1;
            } else {
                right++;
            }            
        }

        return maxVolume;
    }
}
