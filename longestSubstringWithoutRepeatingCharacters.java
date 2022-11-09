class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer>result = new HashMap<Character, Integer>();
        int start = 0;
        int maxlen = 0;
        for(int end = 0; end < s.length(); end++) {
            Character current = s.charAt(end);
            if (result.containsKey(current)) {
                start = Math.max(result.get(current) + 1, start);
            }
            result.put(current, end);
            maxlen = Math.max(end - start + 1, maxlen);
        }
        return maxlen;
    }
}