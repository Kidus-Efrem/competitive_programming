class Solution {
    int iter(int n, const vector<int>& nums) {
        vector<float> dp(n + 1, numeric_limits<float>::infinity());
        dp[1] = 0;

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= nums[i - 1]; j++) {
                if (i + j <= n) {
                    dp[i + j] = min(dp[i] + 1, dp[i + j]);
                }
            }
        }
        return dp[n];
    }

public:
    int jump(vector<int>& nums) {
        return iter(nums.size(), nums);
    }
};
