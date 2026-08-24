"""
two poitner approach
by comparing left (start) and right (end) of the string
if str is empty return false
if left pointer is not letter continue
if right poitner is not letter continue
if left is different of right
    return false
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        s_char = list(s)
        while left < right:
            while left < right and not s_char[left].isalnum():
                left+=1
            while right > left and not s_char[right].isalpha():
                right-=1
            if s_char[left].lower() != s_char[right].lower():
                return False
            
            left, right = left + 1, right - 1
        return True
