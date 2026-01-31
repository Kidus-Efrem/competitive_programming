public class Solution {
    public int LengthOfLongestSubstring(string s) {
        var chars =new HashSet<char>();
      
        int l  = 0;
        int ans = 0;
        for (int i = 0 ; i < s.Length; i++){
            while (l<i && chars.Contains(s[i])){
                chars.Remove(s[l]);
                l+=1;
            }
            chars.Add(s[i]);
            ans = Math.Max(ans, i-l + 1);
        }
        return ans;
    }
}