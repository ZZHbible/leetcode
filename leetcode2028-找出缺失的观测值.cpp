class Solution {
public:
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) {
        int m = rolls.size();
        float sum=mean*(m+n);
        for(auto &i:rolls){
            sum -= i;
        }
        float avg=sum/n;
        vector<int> ans;
        if(avg <1 || avg >6){
            return ans;
        }
        if (avg==floor(avg)){
            return vector<int>(n,int(avg));
        }
        int f=floor(avg);
        int c=ceil(avg);
        int num_f=c*n-sum;
        int num_c=n-num_f;
        for(int i=0;i<num_f;i++){
            ans.emplace_back(f);
        }
        for(int i=0;i<num_c;i++){
            ans.emplace_back(c);
        }
        return ans;
    }
};