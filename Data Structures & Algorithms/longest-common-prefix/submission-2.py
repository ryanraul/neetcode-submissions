class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefixes = {}
        for text in strs:        
            for i in range(len(text)):
                key = text[:i+1]
                prefixes[key] = prefixes.get(key,0) + 1
        
        longest_count = -1
        longest_key = ''
        for prefix in prefixes:
            if prefixes[prefix] > longest_count or (prefixes[prefix] == longest_count and len(prefix) > len(longest_key)):
                longest_count = prefixes[prefix]
                longest_key = prefix

        response = longest_key
        if len(strs) > longest_count:
            response = ''


        return response