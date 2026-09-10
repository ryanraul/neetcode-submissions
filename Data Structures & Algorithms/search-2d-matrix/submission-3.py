"""

- row_size = lend(matrix[0])
- first we try to find the row using binary search
    - l_row = 0
    - r_row = len(matrix) - 1
    - mid_row = (l+r) // 2
    - we can check if the target value is between the first and last column value
    - check if target < mid_row first colum matrix[mid_row][0]
        - yes: we dont need to check the rows below, because they contains bigger values
    - check if target > mid_row last column matrix[mid_row][row_size-1]
        - yes: we don need to check the rows above, because they contins lower values
    
- after locating the right row try to locate the exact column where the value is
    - basically binary search

    - mid_col = (l_col + r_col)//2

    - if matrix[mid_row][mid_col] == target:
        - return True
    
    - if target > matrix[mid_row][mid_col]:
        - l_col = mid_col + 1
    - else:
        - r_col = mid_col - 1
    
return False in case we couldnt locate the target on the matrix

"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_row = 0
        r_row = len(matrix) - 1

        row_size = len(matrix[0])
        mid_row = 0
        while l_row <= r_row:
            mid_row = (l_row + r_row) // 2

            if target < matrix[mid_row][0]:
                r_row = mid_row - 1
            elif target > matrix[mid_row][row_size - 1]:
                l_row = mid_row + 1
            else:            
                break
        
        l_col = 0
        r_col = row_size - 1

        while l_col <= r_col:
            mid_col = (l_col + r_col) // 2

            if matrix[mid_row][mid_col] == target:
                return True
            
            if target > matrix[mid_row][mid_col]:
                l_col = mid_col + 1
            else:
                r_col = mid_col - 1
        
        return False





