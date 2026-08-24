public class Solution {
    public bool IsValid(string s) {
        // create a stack to save each character
        // if its a open character we just push throug the stack
        // it is a close chracter we check if the if the top of the 
            // stack is the open version of this character

        var stack = new Stack<char>();

        foreach(var bracket in s){
            if(!IsOpen(bracket)) {
                if(stack.Count() == 0) return false;

                var poppedValue = stack.Pop();
                if(poppedValue != GetOpenVersion(bracket))
                    return false;
                    
                continue;
            }
            
            stack.Push(bracket);
        }

        return stack.Count() == 0;
    }

    public char GetOpenVersion(char bracket){
        switch(bracket) {
            case ')':
                return '(';
            case ']':
                return '[';
            case '}':
                return '{';
            default: 
                return ' ';
        }
    }
    

    public bool IsOpen(char bracket){
        return bracket == '(' || bracket == '[' || bracket == '{';
    }
}
