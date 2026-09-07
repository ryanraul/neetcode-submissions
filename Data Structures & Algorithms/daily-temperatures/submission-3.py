"""
    
 0  1  2  3  4  5  6
[30,38,30,36,35,40,28]
                *

[5,6]
[1, 4, 1, 2, 1, 0, 0]
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size_temps = len(temperatures)
        res = [0] * size_temps
        stack_temps = []

        for i, t in enumerate(temperatures):

            while stack_temps and temperatures[stack_temps[-1]] < t:
                popped_indice = stack_temps.pop()
                res[popped_indice] = i - popped_indice
            
            stack_temps.append(i)

        return res