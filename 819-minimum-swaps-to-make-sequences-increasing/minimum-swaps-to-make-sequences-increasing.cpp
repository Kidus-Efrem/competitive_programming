#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

class Solution {
public:
    int minSwap(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size();
        

        vector<vector<int>> memo(n, vector<int>(2, -1));
        function<int(int, int)> back = [&](int i, int swapped) -> int {
            if (i == n) {
                return 0;
            }

            if (memo[i][swapped] != -1){
                return memo[i][swapped];
            }
            
            int n1 = nums1[i-1];
            int n2 = nums2[i-1];
            
            if (swapped) {
                int temp = n1;
                n1 = n2;
                n2 = temp;
            }
            

            int ans = 1e9; 
            

            if (nums1[i] > n1 && nums2[i] > n2) {
                ans = back(i + 1, 0);
            }
            if (nums1[i] > n2 && nums2[i] > n1) {
                ans = min(ans, back(i + 1, 1) + 1);
            }
            
            return memo[i][swapped] = ans;
        };

        
        int ans1 = back(1, 0);
        int ans2 = back(1, 1) + 1; 
        
        return min(ans1, ans2);
    }
};