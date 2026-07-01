public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        string alphabets = "abcdefghijklmnopqrstuvwxyz";
        Dictionary<string, List<string>> mapper = new Dictionary<string, List<string>>{};

        for (int i = 0; i < strs.Length; i++)
        {
            int[] curr = new int[26];
            foreach (char ch in strs[i])
            {
                int charIdx = alphabets.IndexOf(ch);
                curr[charIdx] += 1;
            }
            string dictKey = string.Join("-", curr);
            
            if (!mapper.ContainsKey(dictKey))
            {
                mapper[dictKey] = [];
            }
            
            mapper[dictKey].Add(strs[i]);
        }        

        return mapper.Values.ToList();
    }
}
