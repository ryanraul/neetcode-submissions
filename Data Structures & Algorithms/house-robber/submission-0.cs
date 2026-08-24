/*
    [2, 1, 1, 4, 1, 1, 6]


    (6,0)
    (1+0, 6)

    withCurrent = 1 + 0
    withoutCurrent = Max(6,0)

    (1,6)

    (1,6)

    withCurrent = 1 + 6
    withoutCurrent = Max(1,6)

    (7,6)

    4
    withCurrent = 4 + 6
    withoutCurrent = Max(7,6)

    withCurrent = 10
    withoutCurrent = 7
    (10,7)

    Node: 1
    1
    withCurrent = 1 + 7
    withoutCurrent = Max(10,7)
    (8,10)

    Node: 1
    1
    withCurrent = 10 + 1
    withoutCurrent = Max(8,10)
    (11,10)

    Node: 2
    2
    withCurrent = 10 + 2
    withoutCurrent = Max(11,10)

    (12,10)

    Max(12,10)

*/

public class Solution {
    public int Rob(int[] nums) {
        var(withCurrent, withoutCurrent) = DfsRob(0, nums);
        return Math.Max(withCurrent, withoutCurrent);
    }

    public (int withCurrent, int withoutCurrent) DfsRob(int index, int[] nums){
        if(index == nums.Length) return (0,0);

        var(withCurrentSon, withoutCurrentSon) = DfsRob(index + 1, nums);

        var withCurrent = nums[index] + withoutCurrentSon;
        var withoutCurrent = Math.Max(withCurrentSon, withoutCurrentSon);

        return (withCurrent, withoutCurrent);
    }
}
