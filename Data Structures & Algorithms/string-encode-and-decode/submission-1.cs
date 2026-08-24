public class Solution {

    public string Encode(IList<string> strs) {
        var stringsBuilder = new StringBuilder();
        foreach(var s in strs){
            stringsBuilder.Append(s);
            stringsBuilder.Append("/.");
        }

        return stringsBuilder.ToString();
    }

    public List<string> Decode(string s) {
        var stringBuilder = new StringBuilder();
        var stringList = new List<string>();
        var stringsArray = s.ToCharArray();

        for(int i = 0; i < s.Length; i++){  
            if(stringsArray[i] == '/' && stringsArray[i+1] == '.'){
                stringList.Add(stringBuilder.ToString());
                stringBuilder.Clear();
                i++;
                continue;
            }

            stringBuilder.Append(stringsArray[i]);
        }        

        return stringList;
   }
}
