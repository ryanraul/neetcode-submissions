"""
nums=[1, 1, 1, 2, 2, 3]

dic{
    key: counter
    1: 1,
    2: 2
    3: 3
}

array = [[3,1], [2,2]], [1,1]]
array_sorted = [[1,1],[2,2],[3,1]]

response = []
for i in range(len(array), 0, -1):
               key = real number = sub_array[1]
    res.append(array.pop()[1])
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for num in nums:
            if num not in dic:
                dic[num] = 0
            dic[num] += 1

        values = []
        for key, counter in dic.items():
            values.append([counter, key])
        
        values.sort()
        res = []

        for i in range(len(values), 0, -1):
            biggest_counter_subarray = values.pop()
            number_biggest_counter = biggest_counter_subarray[1]
            res.append(number_biggest_counter)
            if(len(res)==k):
                return res

        return []