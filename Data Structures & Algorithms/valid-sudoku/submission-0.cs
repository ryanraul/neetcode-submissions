public class Solution {
    public bool IsValidSudoku(char[][] board) {
        // add column - add row
        // add column - add row

        // Dictionary<> Key - Value
        // Dictionary<int, HashSet<int>>
            // Dic<row, values>
            // Dic<column, values>
        
        var rowsValues = new Dictionary<int, HashSet<char>>();
        var columnValues = new Dictionary<int, HashSet<char>>();
        var blockValues = new Dictionary<int, HashSet<char>>();
        int block = 0;
        int section = 0;

        for(int i = 0; i < 9; i++) {
            if(i % 3 == 0 && i != 0)
                section+=3;
                
            block = section;

            for(int j = 0; j < 9; j++) {
                char currentValue = board[i][j];
                if(j % 3 == 0 && j != 0) block++;

                if(currentValue == '.') continue;

                if(!rowsValues.ContainsKey(i))
                    rowsValues[i] = new HashSet<char>();

                var notDuplicatedRow = rowsValues[i].Add(currentValue);

                if(!columnValues.ContainsKey(j))
                    columnValues[j] = new HashSet<char>();

                var notDuplicatedColumn = columnValues[j].Add(currentValue);

                if(!blockValues.ContainsKey(block))
                    blockValues[block] = new HashSet<char>();

                var notDuplicatedBlock = blockValues[block].Add(currentValue);

                if(!notDuplicatedRow || !notDuplicatedColumn || !notDuplicatedBlock) 
                    return false;
            }
        }

        return true;
    }
}
