/*
    - [2,20,4,10,3,4,5]
    - save all the numbers in a hash set
    - cause aceess for this number in a hash is going to be O(1) constant time complexity
    - check each number in the array
        - if the current number - 1 does not exist in the hash (we found the initial of a possible sequence)
            - size = 1
            - while nubmer + size is in the hashset
                - increment the size
            
            - maxSequence = Max(size, maxSequence)
    - return maxSequence
*/

public class Solution {
    public int LongestConsecutive(int[] nums) {
        HashSet<int> numbersSet = new HashSet<int>(nums);
        int maxSequence = 0;

        foreach(int num in nums){
            if(!numbersSet.Contains(num-1)){
                int size = 0;
                while(numbersSet.Contains(num+size))
                    size++;
                maxSequence = Math.Max(size, maxSequence);
            }
        }
        return maxSequence;
    }
}
