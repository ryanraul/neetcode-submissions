"""
{
    [0,3,2,5,4,6,1,1]
    0: 0, does not have previous value
        so that could be the beggining of a sequence
        lets start to counting the sequence
        length start in 0
        while next value exist in the set
        keep incrementing the lenght
            0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 = size = 
        get the max between current length and the longest
    if the current number does not a previous
        

}
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)    
        longestSeq = 0

        for num in nums:
            if (num - 1) not in setNums:
                lengthSeq = 0
                while (num + lengthSeq) in setNums:
                    lengthSeq += 1

                longestSeq = max(lengthSeq, longestSeq)

        return longestSeq

        