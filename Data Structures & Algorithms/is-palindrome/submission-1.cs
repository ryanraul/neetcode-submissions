
// tab a bat
// ^-------^
//  ^-----^
//   ^---^
//    ^-^
//     ^

// n -> s.lenght
// O(N / 2)

public class Solution {
    public bool IsPalindrome(string s) {
        int beginIndex = 0, endIndex = s.Length - 1;
        var sArray = s.ToCharArray();

        while(beginIndex < endIndex){
            while(beginIndex < endIndex && !isAlpha(sArray[beginIndex]))
                beginIndex++;
            while(endIndex > beginIndex && !isAlpha(sArray[endIndex]))
                endIndex--;
            
            if(char.ToLower(sArray[beginIndex]) != char.ToLower(sArray[endIndex]))
                return false;
            beginIndex++;
            endIndex--;
        }

        return true;
    }

    public bool isAlpha(char value){
        return (
            value >= 'A' && value <= 'Z' || 
            value >= 'a' && value <= 'z' || 
            value >= '0' && value <= '9' 
        );
    }
}
