/*
- create a hashset of integers
- save all non repetitive numbers in this hash
- check each number in the array nums
    - if in the hash


    [2,20,4,10,3,4,5]
    [2][0]
    [10][0]
    
    [0,3,2,5,4,6,1,1]

*/
public class Solution {

    public int LongestConsecutive(int[] nums) {
        var numbers = new HashSet<int>();
        var longest = 0;

        foreach(int num in nums)
            numbers.Add(num);

        foreach(int num in nums) {
            if(!numbers.Contains(num-1)) {
                var length = 1;
                while(numbers.Contains(num+length))
                    length += 1;
                longest = Math.Max(length, longest);                
            }
        }

        return longest;
    }
}
