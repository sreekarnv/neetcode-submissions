public class Solution {

    public string Encode(IList<string> strs) {
        string word = "";
        foreach(string s in strs)
        {
            word = word + s.Length + '#' + s;
        }   

        return word;
    }

    public List<string> Decode(string s) {
        List<string> words = [];
        int currIdx = 0;

        for(int i = 0; i < s.Length; i++)
        {
            if (i < currIdx) continue;

            if (s[i] == '#')
            {
                string wordLenStr = s[currIdx..i];
                if (int.TryParse(wordLenStr, out int wordLen))
                {
                    int startIdx = i + 1;
                    int endIdx = i + 1 + wordLen;
                    string currWord = s[startIdx..endIdx];

                    words.Add(currWord);
                    currIdx = i + 1 + wordLen;
                }
            }
        }

        return words;
    }
}
