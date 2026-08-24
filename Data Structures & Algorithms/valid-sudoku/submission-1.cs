public class Solution {
    public bool IsValidSudoku(char[][] board) {
        var rowsValues = new HashSet<char>[9];
        var columnValues = new HashSet<char>[9];
        var blockValues = new HashSet<char>[9];

        for (int i = 0; i < 9; i++) {
            rowsValues[i] = new HashSet<char>();
            columnValues[i] = new HashSet<char>();
            blockValues[i] = new HashSet<char>();
        }

        for (int row = 0; row < 9; row++) {
            for (int col = 0; col < 9; col++) {
                char currentValue = board[row][col];
                if (currentValue == '.') continue;

                int blockIndex = (row / 3) * 3 + (col / 3);

                if (!rowsValues[row].Add(currentValue) ||
                    !columnValues[col].Add(currentValue) ||
                    !blockValues[blockIndex].Add(currentValue)) 
                    return false;
            }
        }

        return true;
    }
}
