"""
[30,38,30,36,35,40,28]
  0  1  2  3  4  5  6
                    *
[5,6] 
[1,4,1,2,1,0,0]

[1,4,1,2,1,0,0]

- initialize an array response with a total of zeros that is the same of temperatures size
- create an stack to save the indices that does not find the warmer day
- iterate through the temperatures
    - while stack has value and the top value of the stack is smaller than the current value
        - pop the stack indice
        - and calculate the distance between the current indice value and the popped indice
            -res[popped_indice] = current - popped
        
        - append the current indice in the stack
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        i_temps = []
        temps_length = len(temperatures)
        res = [0] * temps_length

        for i, t in enumerate(temperatures):

            while len(i_temps) > 0 and temperatures[i_temps[-1]] < t:
                popped_indice = i_temps.pop()
                res[popped_indice] = i - popped_indice
            
            i_temps.append(i)
            
        return res