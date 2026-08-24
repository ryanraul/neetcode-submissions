public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var valuesWithIndex = new Dictionary<int, int>();

        for(int i = 0; i < nums.Length; i++){
            if(valuesWithIndex.ContainsKey(target - nums[i]))
                return new int[] {valuesWithIndex[target-nums[i]], i};

            valuesWithIndex[nums[i]] = i;
        }

        return new int[] {};

    }
}
