
"""
[1,2,3,4,5]
- Saving the numbers in a hash
    {number: index}

    {
        
        1: 0,
        2: 1, 
    }

- a: current number in interation
- x: number that i need
- t: target
- t = a + x => t - a = x
- Do I have this number x in my dictionary/hash?
    yes: return the current index and index ofr number x (hash[x])
    no: add the current number a in the hash and continue the search


"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for index, num in enumerate(nums):
            dic[num] = index
        
        for i, a in enumerate(nums):
            x = target - a

            if x in dic and i != dic[x]:
                return [i, dic[x]]
            
            dic[a] = i
        
        return [-1,-1]
        