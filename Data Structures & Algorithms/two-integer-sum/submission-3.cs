public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        // dictionary key -> result | value -> index
        // rest = target - value;

        var dicResults = new Dictionary<int, int>();

        for(int i = 0; i < nums.Length; i++){
            var currentValue = nums[i];
            var rest = target - currentValue;

            if(dicResults.ContainsKey(rest)){
                return new int[]{dicResults[rest], i};
            }
    
            dicResults[currentValue] = i;
        }

        return new int[] {};
    }
}
