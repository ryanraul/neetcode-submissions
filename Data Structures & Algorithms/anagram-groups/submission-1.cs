public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        var dicGroup = new Dictionary<string, List<string>>();

        foreach(string s in strs) {
            var sArray = s.ToCharArray();
            Array.Sort(sArray);
            var sSorted = new string(sArray);

            if(!dicGroup.ContainsKey(sSorted)){
                dicGroup[sSorted] = new List<string>();
            }

            dicGroup[sSorted].Add(s);
        }

        return dicGroup.Values.ToList<List<string>>();
    }
}
