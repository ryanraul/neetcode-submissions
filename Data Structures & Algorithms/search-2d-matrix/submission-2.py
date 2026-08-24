"""
You know that each row and row columns is sorted
And that the first integer of every row is greater than the last
 integer of the previous row
Use binary search to find the row first
    while l_row <= r_row
        mid_row = (l_row+r_row)//2
        get the colums of this row
        target is less than the row first element?
            update r_row = mid_row - 1
        target is greater than the row last element?
            update l_row = mid_row + 1
        otherwise:
            the target must be in this row
            because the target does not exceed or fall short of the range of the row
            stop you found the row
    
    l_col = 0
    r_col = len(row) - 1

    while l_col <= r_col:
        mid_col = (l_row+r_row)//2
        target is less than the element at mid_col index?
            update r_col = mid_col - 1
        target is greater than the element at mid_col index?
            update l_col = mid_col + 1
        otherwise:
            the target was found
            return True
    
    return False -- The target was not found

"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_row = 0
        r_row = len(matrix) - 1

        while l_row <= r_row:
            mid_row = (l_row + r_row)//2
            row_cols = matrix[mid_row]
            if target < row_cols[0]:
                r_row = mid_row -1
            elif target > row_cols[-1]:
                l_row = mid_row + 1
            else:
                break

        l_col = 0
        r_col = len(row_cols) - 1

        while l_col <= r_col:
            mid_col = (l_col + r_col)//2

            if target < row_cols[mid_col]:
                r_col = mid_col - 1
            elif target > row_cols[mid_col]:
                l_col = mid_col + 1
            else:
                return True
        
        return False
                
