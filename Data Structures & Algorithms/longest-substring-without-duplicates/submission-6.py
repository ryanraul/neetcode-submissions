"""
using sliding window
l -> window's beginning
r -> window's end

{
    z: 1,
    x: 1,
    y: 1
}

"zxyzxyz"
 l 
   r

        while count[r] > 1:
            count[l] -= 1 -- decrease the count of the character
            l+=1 -- decrease the size of the window
    
        result = max(longest, r - l + 1) -- saving the longest substring without repeating

    return result
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = { }
        l = 0
        result = 0

        for r, c in enumerate(s):
            if c not in count:
                count[c] = 0
            
            count[c] += 1
            
            while count[c] > 1:
                count[s[l]] -= 1
                l+=1
            
            result = max(result, r - l + 1)
        
        return result

            

