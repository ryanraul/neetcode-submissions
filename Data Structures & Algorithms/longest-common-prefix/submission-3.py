"""
3
first_str[0] = b
s = 'bat' -> s[0] = b
s = 'bag' -> s[0] = b
s = 'bank' -> s[0] = b
s = 'band' -> s[0] = b
res = 'b'

s = 'bat' -> s[1] = a
s = 'bag' -> s[1] = a
s = 'bank' -> s[1] = a
s = 'band' -> s[1] = a
res = 'ba'

s = 'bat' -> s[1] = t
s = 'bag' -> s[1] = g

return res = 'ba'

"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        first_str = strs[0]
        for i in range(len(first_str)):
            for s in strs:
                if i == len(s) or s[i] != first_str[i]:
                    return res
            res+=first_str[i]
        return res