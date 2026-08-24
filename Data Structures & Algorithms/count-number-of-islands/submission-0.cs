/*

rows => grid.Length
columsn => grid[0].Length

visited => [...vistedIndexes]

- check each index of the grid
    - current index equals to 1 (land) and its not visited
        - check for the other adjacents lands (dfs)
    

    

*/
public class Solution {
    private HashSet<int> visited = new HashSet<int>();
    private int _rows = 0;
    private int _cols = 0;

    public int NumIslands(char[][] grid) {
        _rows = grid.Length;
        _cols = grid[0].Length;
        int islands = 0;

        for(int i = 0; i < _rows; i++){
            for(int j = 0; j < _cols; j++) {
                var cellIndex = i * _cols + j;

                if(grid[i][j] == '1' && !visited.Contains(cellIndex)){
                    dfs(i, j, grid);
                    islands++;
                }
            }
        }

        return islands;
    }

    public int dfs(int row, int column, char[][] grid){
        var cellIndex = row * _cols + column;
        if(
            row < 0 || 
            row == _rows || 
            column < 0 || 
            column == _cols || 
            grid[row][column] != '1' ||
            visited.Contains(cellIndex)
        )
            return 0;

        visited.Add(cellIndex);

        int numberLands = 1;

        numberLands += dfs(row + 1, column + 0, grid);
        numberLands += dfs(row -1, column + 0, grid);
        numberLands += dfs(row + 0, column + 1, grid);
        numberLands += dfs(row + 0, column -1, grid);

        return numberLands;
    }
}
