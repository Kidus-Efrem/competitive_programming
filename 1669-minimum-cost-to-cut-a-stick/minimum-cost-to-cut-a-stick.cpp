class Solution {
public:
    int minCost(int L, vector<int>& a) {
		sort(a.begin(), a.end());
		vector<int> b;
		int prev = 0;
		for(auto ai: a){
			b.push_back(ai - prev);
			prev = ai;
		}
		b.push_back(L - a.back());
		vector dp(b.size(), vector<int>(b.size(), -1));
		vector<int> pre{0};
		for(auto bi: b) pre.push_back(pre.back() + bi);

		function<int(int,int)> calc = [&](int l, int r){
			if(l == r) return 0;
			if(dp[l][r] != -1) return dp[l][r];
			int mn = INT_MAX;
			for(int i = l; i < r; ++i){
				mn = min(mn, calc(l, i) + calc(i + 1, r));
			}
			dp[l][r] = mn + pre[r + 1] - pre[l];
			return dp[l][r];
		};
		return calc(0, b.size() - 1);
    }
};