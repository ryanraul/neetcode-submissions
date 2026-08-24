/*

    [1,2,3,4]
     ^     ^
     |_____|
        x
    x = 5
    target = 3
    
    call [check indexes function]

    [1,2,3,4]
     ^   ^
     |___|
       x
    x = 4
    target = 3

    call [check indexes function]
    
    [1,2,3,4]
     ^ ^
     |_|
      x
    x = 3
    target = 3

    call [check indexes function]

    [check indexes function]
    if x > target?
        yes: decrement right index;
    else if x < target:
        yes: increment left index;
    else:
        yes: Add both indexes + 1 to the response array
*/
public class Solution {
    public int[] TwoSum(int[] numbers, int target) {
        int left = 0, right = numbers.Length - 1;

        while(left < right){
            int currentSum = numbers[left] + numbers[right];

            if(currentSum > target){
                right--;
            }
            else if (currentSum < target){
                left++;
            } else {
                return new int[]{left + 1, right + 1};
            }
        }

        return new int[]{-1,-1};
    }
}
