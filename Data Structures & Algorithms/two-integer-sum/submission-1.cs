public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var valuesWithIndex = new Dictionary<int, int>();
        int i;
        for(i = 0; i < nums.Length; i++){
            valuesWithIndex.Add(i, nums[i]);
        }

        int keyFounded = default;
        for(i = 0; i < nums.Length; i++){
            var value = target - nums[i];
            keyFounded = valuesWithIndex.FirstOrDefault(x => x.Key != i && x.Value == value).Key;
            if(keyFounded != default) break;
        }

        return new int[] {i, keyFounded};

    }
}
