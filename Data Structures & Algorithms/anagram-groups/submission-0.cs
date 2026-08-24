public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        // ["act","pots","tops","cat","stop","hat"]
        // Dic<0,0>
        // Dic<3,0>
        // Dic<1,1>
        // Dic<2,1>
        // Dic<4,1>
        // Dic<5,4>

        var groups = new Dictionary<int, int>();

        for(int i = 0; i < strs.Length; i++){
            if(groups.ContainsKey(i)) continue;
            groups[i] = i;

            var compareText = strs[i];
        
            for(int j = 0; j < strs.Length; j++){
                if(groups.ContainsKey(j)) continue;
                if(IsAnagram(compareText, strs[j]))
                    groups[j] = i;
            }
        }

        int currentGroup = -1;

        var groupsList = new List<List<string>>();
        var currentGroupList = new List<string>();
        // -1 != 0 -> create a new list
        // 0 == 0 -> add this index on the list

        // currentGroup = -1 | element.Key = 0 | element.Value = 0
            // if(true) => currentGroupList[] | groupsList[['act']] | currentGroupList['act']
        // currentGroup = 0 | element.Key = 3 | element.Value = 0
            // if(false) => currentGroupList['act'] | groupsList[['act', 'cat']] | currentGroupList['act', 'cat']
        // currentGroup = 0 | element.Key = 0 | element.Value = 1
            // if(true) => currentGroupList[] | groupsList[['act', 'cat'], ['pots']] | currentGroupList['pots']
        // currentGroup = 1 | element.Key = 3 | element.Value = 1
            // if(false) => currentGroupList['pots'] | groupsList[['act', 'cat'], ['pots','tops']] | currentGroupList['pots', 'tops' ]
        
        foreach(var element in groups){

            if(currentGroup != element.Value){
                currentGroup = element.Value;
                currentGroupList = new List<string>();
                groupsList.Add(currentGroupList);
            }

            currentGroupList.Add(strs[element.Key]);
        }

        return groupsList;
    }

    public bool IsAnagram(string text1, string text2){
        if(text1.Length != text2.Length)
            return false;

        var arrayText1 = text1.ToCharArray();
        var arrayText2 = text2.ToCharArray();

        Array.Sort(arrayText1);
        Array.Sort(arrayText2);

        for(int i = 0; i < text1.Length; i++){
            if(arrayText1[i] != arrayText2[i]) return false;
        }

        return true;
    }
}
