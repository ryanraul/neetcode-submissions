/*
    
    - maxIslandArea = 0;

    - check all the cells with equals to 1
        maxIslandArea = Max(maxIslandArea, dfs())
    
    return maxIslandArea

    - dfs
        - stop criterea: invalid row or col || visited || grid[row][col] != 1

        - add to visited
        - islandCells = 1

        - foreach directions
            - islandCells += dfs

        - islandCells


    [0,1,1,0,1],
    [1,0,1,0,1],
    [0,1,1,0,1],
    [0,1,0,0,1]

    visited[0,1] | isLandCell = 1 + back = 6
    visited[0,2] | islandCell = 1 + back = 5
    visited[1,2] | islandCell = 1 + back = 4
    visited[2,2] | islandCell = 1 + back = 3
    visited[2,1] | islandCell = 1 + back = 2
    visited[3,1] | islandCell = 1

    return 6

    
*/

public class Solution {
    private bool[,] visited;
    private int rows = 0, columns = 0;

    public int MaxAreaOfIsland(int[][] grid) {
        rows = grid.Length;
        columns = grid[0].Length;
        visited = new bool[rows, columns];
        int maxAreaIsland = 0;

        for(int row = 0; row < rows; row++){
            for(int col = 0; col < columns; col++){
                if(grid[row][col] == 1){
                    maxAreaIsland = Math.Max(maxAreaIsland, Dfs(row, col, grid));
                }
            }
        }

        return maxAreaIsland;
    }

    public int Dfs(int row, int col, int[][] grid){
        if(
            row < 0 || 
            col < 0 || 
            row == rows || 
            col == columns ||
            grid[row][col] != 1 ||
            visited[row,col]
        )
            return 0;

        int islandCells = 1;
        visited[row,col] = true;

        islandCells += Dfs(row + 1, col + 0, grid);
        islandCells += Dfs(row + -1, col + 0, grid);
        islandCells += Dfs(row + 0, col + 1, grid);
        islandCells += Dfs(row + 0, col + -1, grid);

        return islandCells;
    }
}
