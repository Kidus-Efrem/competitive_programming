public class Solution {
    public int NumSubmat(int[][] mat) {
        
        for (int i =0; i < mat.Length; i++){
            for (int j = 0; j < mat[i].Length; j++){
                if (j-1 >= 0 && mat[i][j] >0){
                    mat[i][j] += mat[i][j-1];
                }
            }
        }
        int ans = 0;
        for ( int j = 0; j < mat[0].Length; j++){
            int top = 0;
            for (int i = 0; i < mat.Length; i++){
                int mn = int.MaxValue;
                if (mat[i][j] == 0){
                    continue;
                }

                for (int k = i; k < mat.Length; k++){

                    if (mat[k][j] == 0){
                        break;
                    }
                    mn = Math.Min(mat[k][j], mn);
                    ans +=mn;

                }
            }

        }
        
        return ans;
    }
}