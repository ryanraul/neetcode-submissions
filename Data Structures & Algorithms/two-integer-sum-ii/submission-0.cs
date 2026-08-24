/*

    target = number + number
    number = target - number;

    [1,2,3,4]
    [1,3,4,5,6]
    
    rest for 1 = 8
    6 < 8
    1 cannot be used
    increment index1

    rest for 6 = 3
    3 > 1
    maybe we have a 3 do nothing to index 2
    
    rest for 3 = 6
    6(index2) == 6
    we found

    target = 9

    [1,2,3,4]
    target = 3
    index1 = 1
    index2 = 4

    rest for 1 = 2
    2 < 4 (index2)
    4 cannot be used decrement index 2

    rest for 4 = 3
    3 > 1
    maybe we have keep index 1

    rest for 3 = 2
    2 < 3
    3 cannot be used decrement index 2

    keep index 1

    rest for 2 = 1
    1 == 1(index1)

    2,5

    [1,2,3,4]
    rest of [1] with the biggest value in the array
    rest of [1] > the biggest in the array
    rest of [1] cannot be used so increment

    rest of [last] with the smaller value in the array
    resf of [last] < the smaller value in the array
    rest of [last] cannot be used so decrement
    
    iteration 1: 2 > 4 -> do nothing
    iteration 1: (3 - 4) -1 < 1 -> decrement index, the last cannot be used (lastIndex--;)
    
    iteration 2: 2 > 3 -> do nothing
    iteration 2: (3-3) 0 < 1 -> decrement index, the last cant be used (lastIndex--;)

    iteration 3: 2 > 2 -> they are equals and different indexes return the both current indexes;


    target = 3
    number = 3 - 1 = 2
    we have 2 in the array
*/
public class Solution {
    public int[] TwoSum(int[] numbers, int target) {
        int initialIndex = 0, lastIndex = numbers.Length - 1;

        while(initialIndex < lastIndex) {
            var restInitial = target - numbers[initialIndex];
            var restLast = target - numbers[lastIndex];
            var initialIncrement = 0;
            var lastDecrement = 0;

            if(target == (numbers[initialIndex] + numbers[lastIndex]))
                return new int[]{ initialIndex + 1, lastIndex + 1 };

            if(restInitial > numbers[lastIndex]){
                initialIncrement = 1;
            }

            if(restLast < numbers[initialIndex]){
                lastDecrement = 1;
            }

            initialIndex += initialIncrement;
            lastIndex -= lastDecrement;
        }

        return new int[] {-1, -1};

    }
}
