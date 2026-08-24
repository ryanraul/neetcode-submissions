public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var dic = new Dictionary<int, int>();
        int i;
        for(i = 0; i < nums.Length; i++){
            dic.Add(i, nums[i]);
        }       

        int aux;
        int j = default;
        for(i = 0; i < nums.Length; i++){
            aux = target - nums[i];
            j = dic.FirstOrDefault(x => x.Key != i && x.Value == aux).Key;
            if(j != default) break;
        }

        return new int[] { i, j };
    }
}
