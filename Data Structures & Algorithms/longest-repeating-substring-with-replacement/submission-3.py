"""
"AAABABB"
    l
       r  

size_window = 4
freq_char = 3
replacements = 1
k = 1

using window substring
- save the frequency of the window's characters
- get the most frequent character
- calculate how many replacements have been done
    - replacements = size_window - most_frequent_char
    - if repacements > k:
        - its necessary decrease the window size

"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        l = 0
        longest_window = 0
        replacements = 0

        for r, c in enumerate(s):
            if c not in counter:
                counter[c] = 0

            counter[c] += 1

            while ((r - l + 1) - max(counter.values())) > k:
                counter[s[l]] -= 1
                l += 1

            longest_window = max(longest_window, r - l + 1)
        return longest_window
                         