"""
how do i know which line am i?
    0 - 0, 1, 2...
    1 - 0, 1, 2...
    2 - 0, 1, 2...
which line i should search?
lrow = 0
rrow = 2
0 + 2 // 2 = 1
1 -> 
    lcol = 0 and rcol = 3
    target is between colums[lcol] and columns[rcol]?
    use binary search to try to locate the target


[
    [1, 3, 5, 7],
    [10,11,16,20],
    [23,30,34,60]
]

13

"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_row = 0
        r_row = len(matrix) - 1

        while l_row <= r_row:
            mid_row = (l_row+r_row)//2
            
            cols = matrix[mid_row]
            l_col, r_col = 0, len(cols)-1
            
            if cols[l_col] <= target and cols[r_col] >= target:
                while l_col <= r_col:
                    mid_col = (l_col+r_col)//2

                    if cols[mid_col] == target:
                        return True
                    elif target < cols[mid_col]:
                        r_col = mid_col - 1
                    else:
                        l_col = mid_col + 1
                return False
            elif cols[l_col] > target:
                r_row = mid_row - 1
            else:
                l_row = mid_row + 1

        return False
                
