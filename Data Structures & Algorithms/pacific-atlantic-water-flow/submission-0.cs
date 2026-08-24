public class Solution {
    private int rows = 0, columns = 0;
    private bool[,] visited;

    public List<List<int>> PacificAtlantic(int[][] heights) {
      rows = heights.Length;
      columns = heights[0].Length;
      visited = new bool[rows,columns];

      List<List<int>> validCells = new List<List<int>>();

      for(int row = 0; row < rows; row++){
        for(int col = 0; col < columns; col++){
          var(atlanticReach, pacificReach) = dfs(row, col, heights, heights[row][col]);
          if(atlanticReach && pacificReach)
            validCells.Add(new List<int> { row, col });
        }
      }

      return validCells;
    }

    public (bool atlanticReach, bool pacificReach) dfs(int row, int col, int[][] heights, int parentHeight) {
      var atlanticReach = row == rows || col == columns;
      var pacificReach = row < 0 || col < 0;

      if(atlanticReach || pacificReach || visited[row,col] || heights[row][col] > parentHeight)
        return (atlanticReach, pacificReach);

      visited[row,col] = true;
      
      int[][] directions = new int[][] {
            new int[] { 0, 1 },
            new int[] { 0, -1 },
            new int[] { 1, 0 },
            new int[] { -1, 0 }
        };

      foreach(var dc in directions){
        if(atlanticReach && pacificReach)
          break;
        
        var(resAtlantic, resPacific) = dfs(row+dc[0], col+dc[1], heights, heights[row][col]);
        atlanticReach = resAtlantic ? resAtlantic : atlanticReach;
        pacificReach = resPacific ? resPacific : pacificReach;
      }

      visited[row,col] = false;

      return (atlanticReach, pacificReach); 
    }
}
