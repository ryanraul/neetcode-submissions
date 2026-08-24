/*
    - using a tree based solution
    - we can calculate how much parentheses we have
    - we can calculate how much closed parenthes we have

    - if (close + open) == size
        - add the current string to the response list  

    - if close <= open
        - add a new close parenthesis in the current string and pass to the method
    
    - if open < size
        - add a new open parenthesis in the current string and pass to the method
*/
public class Solution {  
    private int size;
    private List<string> response = new List<string>();

    public List<string> GenerateParenthesis(int n) {
        size = n;
        if(n>0)
            GeneratePossibilities(1,0,"(");

        return response;
    }

    public void GeneratePossibilities(int open, int close, string current){
        if((open+close) == size * 2){
            response.Add(current);
            return;
        }

        if(close < open)
            GeneratePossibilities(open, close + 1, $"{current})");

        if(open < size)
            GeneratePossibilities(open + 1, close, $"{current}(");
    }
}
