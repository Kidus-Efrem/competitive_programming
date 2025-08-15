class Solution {
public:
    int minDistance(string word1, string word2) {
        int n = word2.size();
        int m = word1.size();

        // dp[i][j] = min operations to convert first i chars of word2
        // to first j chars of word1
        vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));

        // Initialize first row and first column
        for (int i = 0; i <= n; i++)
            dp[i][0] = i; // delete all characters from word2
        for (int j = 0; j <= m; j++)
            dp[0][j] = j; // insert all characters to word2

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (word2[i - 1] == word1[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1]; // no operation needed
                } else {
                    dp[i][j] = 1 + min({
                        dp[i - 1][j],    // delete
                        dp[i][j - 1],    // insert
                        dp[i - 1][j - 1] // replace
                    });
                }
            }
        }

        return dp[n][m];
    }
};
