
"""

AAABABB
l   r
k = 1
counter {
    a: 4,
    b: 1
}

5 - 4 = 1 > 1




for r in range(len(s))
    windowSize = r - l + 1
    lessCharacterCount = min(counter.values)
    result = windowSize - lessCharacterCount
    while result > k:
        decrement left character count
        increment left pointer

    res = max(res, windowsSize)
return res

"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        counter = {}
        res = 0
        for r in range(len(s)):
            if s[r] not in counter:
                counter[s[r]] = 0
            counter[s[r]] += 1

            while ((r - l + 1) - max(counter.values())) > k:
                counter[s[l]] -= 1
                l+=1

            res = max(res, r - l + 1)
        return res

        