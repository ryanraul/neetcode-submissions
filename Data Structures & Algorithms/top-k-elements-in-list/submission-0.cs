public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        // Create a dic<int, int>
            // Key: the number
            // Value: frequency of this number

        var frequentNumbers = new Dictionary<int, int>();

        foreach(var num in nums){
            if(!frequentNumbers.ContainsKey(num))
                frequentNumbers[num] = 0;
            frequentNumbers[num]++;
        }

        return frequentNumbers
            .OrderByDescending(x => x.Value)
            .Take(k)
            .Select(x => x.Key)
            .ToArray();
    }
}
