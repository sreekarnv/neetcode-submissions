public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length) return false;
        Dictionary<char, int> count = new Dictionary<char, int> {};

        for(int i = 0; i < s.Length; i++)
        {
            if (!count.ContainsKey(s[i]))
            {
                count.Add(s[i], 0);
            }

            count[s[i]] += 1;        
        }

        foreach(char j in t)
        {
            if (!count.ContainsKey(j)) return false;
            count[j] -= 1;

            if (count[j] == 0)
            {
                count.Remove(j);
            }
        }

        return count.Count == 0;
    }
}
