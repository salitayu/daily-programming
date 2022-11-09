public class Solution {
    public int LengthOfLongestSubstring(string s) {
        int maxlen = 0;
        int start = 0;
        Dictionary<Char, int> counts = new Dictionary<Char, int>();
        for(int end = 0; end < s.Length; end++) {
            Char current = s[end];
            if (counts.ContainsKey(current)) {
                start = Math.Max(start, counts[current]+1);
            }
            counts[current] = end;
            maxlen = Math.Max(end - start + 1, maxlen);
        }
        return maxlen;
    }
}