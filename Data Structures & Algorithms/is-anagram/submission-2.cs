public class Solution {
    public bool IsAnagram(string s, string t) {
        if(s.Length != t.Length) return false;

        var sSorted = s.ToCharArray();
        var tSorted = t.ToCharArray();
        Array.Sort(sSorted);
        Array.Sort(tSorted);

        for(int i = 0; i < s.Length; i++){
            if(sSorted[i] != tSorted[i])
                return false;
        }

        return true;
    }
}
