// rows -> matrix.length
// columns -> matrix[0].length

// start => 0
// end => row - 1

// loop start < end
    // med => (start + end) / 2
    
    // target is between matrix[med][0] and matrix[med][columns-1]
        // we have the row
    // target > matrix[med][0]
        // start = med + 1
    // target < matrix[med][0]
        // end = med - 1 

// start = 0
// end = columns -1
// loop start < end
    // med => (start + end) / 2
    
    // target == matrix[row][med]
        // we have the row
    // target > matrix[row][med]
        // start = med + 1
    // target < matrix[row][med]
        // end = med - 1 

// start => 0
// end => 2

// loop start <= end
    // med = 0 + 2/ 2 = 1

    // 10 is between 10 and 13
        // we found the row


// start => 0
// end => 3

// loop start <= end
    // med = 0 + 3 / 2 = 1

    // 10 > 11 : X
    // 10 < 11
        // end = 1 - 1 => 0
    
    // iteration 2
    // med => 0 + 0 / 2 = 0

    // 10 == 10
        // return true

/*

[
    [01,03,05,07],
    [10,11,16,20],
    [23,30,34,60]]

    0 + 2
    2 / 2 = 1
 
    13 is between 10 an 20

    selectedRow = 1

    0 + 3
    3 / 2 = 1

    13 == 11
    13 > 11 
        start = 1 + 1 = 2

    med = 2 + 2 / 2 = 2

    13 == 16: X
    13 > 16:
    13 < 16:
        end = 2 - 1 = 1
    
*/



public class Solution {
    public bool SearchMatrix(int[][] matrix, int target) {
        int rows = matrix.Length;
        int columns = matrix[0].Length;
        int start = 0, end = rows -1, med = 0;
        int selectedRow = -1;

        while(start <= end){
            med = (start + end) / 2;

            if(target >= matrix[med][0] && target <= matrix[med][columns - 1])
            {
                selectedRow = med;
                break;
            }
            else if(target > matrix[med][0])
                start = med + 1;
            else
                end = med - 1;
        }

        if(selectedRow < 0)
            return false;

        start = 0;
        end = columns - 1;
        while(start <= end){
            med = (start + end) / 2;

            if(target == matrix[selectedRow][med])
                return true;
            else if(target > matrix[selectedRow][med])
                start = med + 1;
            else
                end = med - 1;
        }

        return false;
    }
}



