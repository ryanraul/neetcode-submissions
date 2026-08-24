/*
    - we could use the two pointers approach
    - one represent maximum value in the left - the first element in the array
    - one represent maximum value in the right - the last element in the array
    - if the max left is less than max right
    - increase left pointer and add up to the response the difference between maxLeft - currentLeft
    - otherwise decrease right pointer and add up to the response the diff between maxRight - currentRight

*/
public class Solution {
    public int Trap(int[] height) {
        int left = 0, right = height.Length - 1;
        int maxLeft = 0, maxRight = 0;
        int response = 0;

        while(left < right) {
            maxLeft = Math.Max(maxLeft, height[left]);
            maxRight = Math.Max(maxRight, height[right]);

            if(maxLeft < maxRight){
                left++;
                response += Math.Max(0, maxLeft - height[left]);
            } else {
                right--;
                response += Math.Max(0, maxRight - height[right]);
            }
        }

        return response;

    }
}
