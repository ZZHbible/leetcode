class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        vector<vector<int>>dp(triangle.size(),vector<int>(triangle[triangle.size()-1].size(),INT_MAX));
        dp[0][0]=triangle[0][0];
        for(int i=1;i<triangle.size();i++){
            for(int j=0;j<triangle[i].size();j++){
                if(j==0){
                    dp[i][j]=dp[i-1][j]+triangle[i][j];
                }
                else{
                    dp[i][j]=min(dp[i-1][j],dp[i-1][j-1])+triangle[i][j];
                }
            }
        }
        int ans=INT_MAX;
        for(int i:dp[triangle.size()-1]){
            ans=min(ans,i);
        }
        return ans;
    }
};