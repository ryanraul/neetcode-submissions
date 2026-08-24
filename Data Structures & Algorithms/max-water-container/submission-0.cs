/*
 - we could apply the two pointers approach
 - two pointers 
    - left
    - right

 - Calculate the volume while we decrease both index pointers
 - Saving always the maximum volume found it and the height indexes

 - Icrement or decrement the smaller height of the index side
 - Decrement the width between the pointers

 - [1,7,2,5,4,7,3,6]
    ^             ^
    |_____________|
           7

    volume = Min(1(left),6(right)) * 7 (width) = 7
    maximum = 7
 - [1,7,2,5,4,7,3,6]
      ^           ^
      |___________|
           6

    volume = Min(7(left),6(right)) * 6 (width) = 36
    maximum = 36

 - [1,7,2,5,4,7,3,6]
      ^         ^
      |_________|
           5

    volume = Min(7(left),3(right)) * 5 (width) = 15
    maximum = 36
    
 - [1,7,2,5,4,7,3,6]
        ^     ^
        |_____|
           3

    volume = Min(2(left),7(right)) * 3 (width) = 6
    maximum = 36
*/
public class Solution {
    public int MaxArea(int[] heights) {
        int left = 0, right = heights.Length -1;
        int width = heights.Length - 1;
        int maxVolume = 0;

        while(left < right){
            int currentVolume = Math.Min(heights[left], heights[right]) * width;

            if(currentVolume > maxVolume)
                maxVolume = currentVolume;
            
            if(heights[left] >= heights[right]){
                right--;
            } else {
                left++;
            }

            width--;
        }

        return maxVolume;
    }
}
