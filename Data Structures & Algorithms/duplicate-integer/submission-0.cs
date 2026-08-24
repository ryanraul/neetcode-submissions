public class Solution {
    public bool hasDuplicate(int[] nums) {
        var seen = new HashSet<int>();

        foreach(int num in nums){
            if(!seen.Contains(num))
                seen.Add(num);
            else
                return true;
        }
        
        return false;
    }
}
