/*
    - the values are sorted
    - find the target
    
    - binary search => while left >= right
        - med = (left + right) / 2

        - nums[med] == target
            - return the value
        - target > nums[med]
            - left = med + 1
        - else
            - right = med - 1
*/

public class Solution {
    public int Search(int[] nums, int target) {
        int left = 0, right = nums.Length - 1, med = 0;

        while(left <= right){
            med = (left + right) / 2;

            if(target == nums[med]) {
                return med;
            } else if (target > nums[med]){
                left = med + 1;
            } else {
                right = med - 1;
            }
        }

        return -1;
    }
}
