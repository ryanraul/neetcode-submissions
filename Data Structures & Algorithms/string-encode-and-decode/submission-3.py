"""

create a separate parameter = "#_#"
for each string append the strings with the separator at the end


Hello#_#World
l
        r

"""


class Solution:
    separator = "#"

    def encode(self, strs: List[str]) -> str:
        texts_separators = []
        for text in strs:
            texts_separators.append(str(len(text)))
            texts_separators.append(self.separator)
            texts_separators.append(text)

        response = "".join(texts_separators)
        print(response)
        return response

    def decode(self, s: str) -> List[str]:
        l = 0
        r = 0
        response = []

        while l < len(s) - 1:
            r = l
            while s[r] != self.separator:
                r += 1
            
            size = int(s[l:r])
            l = r + 1
            r = l + size
            print(r)
            response.append(s[l:r])
            l = r
        
        return response
