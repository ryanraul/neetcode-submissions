public class Solution {
    public bool hasDuplicate(int[] nums) {
        var uniqueValues = new HashSet<int>();

        foreach(int num in nums){
            if(!uniqueValues.Add(num))
                return true;
        }

        return false;
    }
}
