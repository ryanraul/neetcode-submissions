/*
[
    [1,1,0],
    [0,1,1],
    [0,1,2]

    [1,1,0],
    [0,1,2],
    [0,2,2]

    [1,1,0],
    [0,2,2],
    [0,2,2]

    [1,2,0],
    [0,2,2],
    [0,2,2]

    [2,2,0],
    [0,2,2],
    [0,2,2]


    scenario 2:

    [2,1,0],
    [0,1,1],
    [0,1,2]

    [2,2,0],
    [0,1,2],
    [0,2,2]

    [2,2,0],
    [0,2,2],
    [0,2,2]
]

 - Breadth first search (BFS)
 - queue([row,visited])
 - visited[row,col]

 - for each element in the matrix
    - freshSize increment
    - if its a rotten fruit
        - enqueue the element

 - while queue is not empty
    - get current queue size
    - for each element in the queue by the queue size
        - dequeue the vaue
        - add to the visit
        - transform to a rotten fruit
        - freshSize --
        - for all the neighbors (directions)
            - if not visited and valid row and col and fresh fruit
                - enqueue the value
        -
    - time ++
*/

public class Solution {
    public int OrangesRotting(int[][] grid) {
        int rows = grid.Length, columns = grid[0].Length;
        int freshSize = 0, time = 0;
        var fruits = new Queue<int[]>();

        for(int row = 0; row < rows; row++){
            for(int col = 0; col < columns; col++){

                if(grid[row][col] == 1){
                    freshSize++;
                } 
                
                if(grid[row][col] == 2){
                    fruits.Enqueue(new int[] {row, col});
                }
            }
        }

        int[][] directions = {
                new int[] {0,1}, new int[] {0,-1},
                new int[] {1,0}, new int[] {-1,0}
            };

        while(fruits.Count > 0 && freshSize > 0){
            var queueSize = fruits.Count;
            for(int i = 0; i < queueSize; i++){
                var fruitIndexes = fruits.Dequeue();
                var row = fruitIndexes[0];
                var col = fruitIndexes[1];

                foreach(var dc in directions){
                    var rowDc = row + dc[0];
                    var colDc = col + dc[1];

                    if(
                        rowDc < 0 ||
                        colDc < 0 ||
                        rowDc == rows ||
                        colDc == columns ||
                        grid[rowDc][colDc] != 1
                    )
                        continue;
                    
                    grid[rowDc][colDc] = 2;
                    fruits.Enqueue(new int[] {rowDc, colDc});
                    freshSize--;
                }
            }
            time++;
        }

        return freshSize == 0 ? time : -1;

    }
}









