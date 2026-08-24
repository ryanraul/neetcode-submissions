"""

for str in strs:
    str_sorted = sorted(str)

    if str_sorted not in dic:
        dic[str_sorted] = []

    dic[str_sorted].append(str)

    return [dic.values]

{
    "act": ["act", "cat"],
    "opst": ["stop", "pots", "tops"]
    ...
}


"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = {}

        for text in strs:
            text_sorted = "".join(sorted(text))

            if text_sorted not in dic:
                dic[text_sorted] = []

            dic[text_sorted].append(text)
        
        response = []
        for values in dic.values():
            response.append(values)

        return response