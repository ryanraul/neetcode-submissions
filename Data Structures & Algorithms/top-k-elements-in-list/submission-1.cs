public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        var dicCounter = new Dictionary<int, int>();

        for(int i = 0; i < nums.Length; i++){
            if(!dicCounter.ContainsKey(nums[i])){
                dicCounter[nums[i]] = 0;
            }

            dicCounter[nums[i]]++;
        }

        return dicCounter
            .OrderByDescending(x => x.Value)
            .Take(k)
            .Select(x => x.Key)
            .ToArray();
    }
}
