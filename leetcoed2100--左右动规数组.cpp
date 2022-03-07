class Solution {
public:
    vector<int> goodDaysToRobBank(vector<int>& security, int time) {
        int len=security.size();
        vector<int> left(len);
        vector<int> right(len);
        left[0]=0;
        right[len-1]=0;
        for(int i=1;i<len;i++){
            if (security[i]<=security[i-1]){
                left[i]=left[i-1]+1;
            }
            else left[i]=0;
            if (security[len-i-1]<=security[len-i]){
                right[len-i-1]=right[len-i]+1;
            }
            else right[len-i-1]=0;
        }
        vector<int> ans;
        for(int i=0;i<len;i++){
            if (left[i]>=time && right[i]>=time){
                ans.emplace_back(i);
            }
        }
        return ans;
    }
};