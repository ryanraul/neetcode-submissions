public class Solution {
    private const string SEPARATOR = "./";
    public string Encode(IList<string> strs) {
        var stringBuilder = new StringBuilder();

        foreach(var str in strs){
            stringBuilder.Append(str);
            stringBuilder.Append(SEPARATOR);
        }

        return stringBuilder.ToString();
    }

    public List<string> Decode(string s) {
        var stringArray = s.ToCharArray();
        var allStrings = new List<string>();
        var stringBuilder = new StringBuilder();

        for(int i = 0; i < stringArray.Length; i++){
            if(stringArray[i] == '.' && stringArray[i+1] == '/'){
                allStrings.Add(stringBuilder.ToString());
                stringBuilder.Clear();
                i++;
                continue;
            }

            stringBuilder.Append(stringArray[i]);
        }

        return allStrings;
    }
}
