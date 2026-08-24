/*
- iterate each number in the array
- i = number in the first loop iterations
    - left = i + 1 and right = size - 1
    - find left and right using the two sums approach
    - target = -[i]value
    - while left < right
        - if([left]value + [right]value == target)
            - Add the indexes
        - else if ([left]value+[right]value < target)
            - Increment left 
        - else
            - Decrement right
*/
public class Solution {
    public List<List<int>> ThreeSum(int[] nums) {
        int size = nums.Length;
        var listThreeSum = new List<List<int>>();
        Array.Sort(nums);

        for(int i = 0; i < size; i++){
            if(i > 0 && nums[i] == nums[i-1])
                continue;

            int left = i + 1; 
            int right = size - 1;
            
            while(left < right){
                int threeSum = nums[i] + nums[left] + nums[right];
                if(threeSum == 0){
                    listThreeSum.Add(new List<int>(){ nums[i], nums[left], nums[right] });
                    left++;
                    while(left < right && nums[left] == nums[left-1]){
                        left+=1;
                    }
                } else if (threeSum < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return listThreeSum;
    }
}
