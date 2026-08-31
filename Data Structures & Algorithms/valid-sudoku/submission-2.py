"""
- valid rows
    - fill the values for each row
    - [[1,2,3], [4,5], ...]
- valid columns
    - fill the values for each columns
    - [[1,4,5,7], [2,9], ...]
- valid boxes
    - fill the values for each boxes
    - [[1,2,4,9,8],[3,5]]
    - which box my value belongs?
    - box_index = board_row * (i / 3)

    - 0 * (0 / 3) = 0
    - 0 + (5/3) = 1
    - 0 + (6/3) = 2
    - (6/3) * 3  + (5/3) = 7
    (row/3) * 3 + (col/3) = 
    
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid_rows = [[0] for _ in range(9)]
        valid_cols = [[0] for _ in range(9)]
        valid_boxes = [[0] for _ in range(9)]

        print(valid_rows)

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == ".":
                    continue

                current_value = int(board[row][col])
                box = (row//3) * 3 + (col//3)
                #print("row: ", row, " | ", "col: ", col, " | ", "box: ", box, " | ", "val: ", current_value)

                if current_value in valid_rows[row]:
                    print(valid_rows)
                    print("row validation")
                    return False
                
                if current_value in valid_cols[col]:
                    print("col validation")
                    return False

                if current_value in valid_boxes[box]:
                    print("box validation")
                    return False 

                print(valid_rows[row])
                valid_rows[row].append(current_value)
                valid_cols[col].append(current_value)
                valid_boxes[box].append(current_value)

        return True