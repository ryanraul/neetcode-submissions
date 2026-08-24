# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

"""
we can use binary search

left = 1
right = n

while left <= right: 
    mid = (left+right)//2
    try guess mid -> guess(mid)
    guess response is equal to zero
        we found it
    
    guess_res is greater than zero
        update left with mid + 1
    otherwise gues_res is smaller than zero
        update right with mid - 1

"""
class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left <= right: 
            mid = (left+right)//2
            res_guess = guess(mid)

            if  res_guess == 0:
                return mid

            if res_guess > 0:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1