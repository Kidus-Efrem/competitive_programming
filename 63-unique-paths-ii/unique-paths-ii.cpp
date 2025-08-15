class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int n = obstacleGrid.size();
        int m  = obstacleGrid[0].size();
        vector<vector<int>>dp(n, vector<int>(m, 0));
        dp[0][0] =1;
        if (obstacleGrid[n-1][m-1] ==1)
            return 0;
        
        for (int i = 0; i< n; i++){
            for (int j = 0; j< m; j++){
                if( obstacleGrid[i][j] != 1){
                if (i-1 >-1 && obstacleGrid[i-1][j]!=1){
                    dp[i][j] += dp[i-1][j];
                }
                if( j-1 > -1 && obstacleGrid[i][j-1]!=1){
                    dp[i][j] += dp[i][j-1];
                }}
            }
        }
        return dp[n-1][m-1];
    }
};