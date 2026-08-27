"""

create dictionary
{
    1: 3,
    2: 2,
    1: 1
}


iterate through each item
- key, counter in dic.items()

create an array to add the counter and order

sort the array

itarate through the sorted array but in reverse order
for i in range(len(sorted_array) - 1, 0, -1)
    add the keys in another array for the response
    if the response array size reach the maximum which is k:
        return


"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic_counters = {}

        for num in nums:
            if num not in dic_counters:
                dic_counters[num] = 0
            dic_counters[num] +=1

        aux_array = []
        for key, counter in dic_counters.items():
            aux_array.append([counter, key])

        sorted_array = sorted(aux_array)
        response = []
        
        for i in range(len(sorted_array), 0, -1):
            aux_values = sorted_array[i - 1]
            response.append(aux_values[1])
            if(len(response) == k):
                return response

        return response    

