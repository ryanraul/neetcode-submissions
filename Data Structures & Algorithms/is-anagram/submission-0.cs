public class Solution {
    public bool IsAnagram(string s, string t) {
        // check if the size is different => false
        // reorder the characters inside the string
            // and compare each to other

        if(s.Length != t.Length) return false;

        var sArray = s.ToCharArray();
        var tArray = t.ToCharArray();
        Array.Sort(sArray);
        Array.Sort(tArray);

        for(int i = 0; i < s.Length; i++){
            if(sArray[i] != tArray[i]) return false;
        }

        return true;
    }
}
