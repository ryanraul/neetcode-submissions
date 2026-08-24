/*


 - 3
 - ["((()))","(()())","(())()","()(())","()()()"]

                        ( - 1 , 0
                            (( - 2, 0



 - if open + close == 2 * n
    - add to the array response
    - return

 - if close < open
    - we can add close parenthesis
    - right = currentString + ")"
 - if open < n
    - we can add open parenthesis
    - left = currentString + "("
 
*/
public class Solution {  
    private List<string> response = new List<string>();
    private int size;

    public List<string> GenerateParenthesis(int n) {
        size = n;
        if(n > 0){
            var initial = "(";
            CreateCombinations(1,0,initial);
        }

        return response;
    }

    public void CreateCombinations(int open, int close, string current){
        if((open + close) == (size*2)){
            response.Add(current);
            return;
        }

        if(close < open){
            var left = $"{current})";
            CreateCombinations(open, close+1, left);
        }

        if(open < size){
            var right = $"{current}(";
            CreateCombinations(open+1, close, right);
        }
    }
}
