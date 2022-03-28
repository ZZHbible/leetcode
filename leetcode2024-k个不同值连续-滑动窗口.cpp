class Solution {
public:
    void check(string answerKey,int k,int &ans,char ch1){
        int begin=0;
        int end=0;
        while (end < answerKey.length()){
            if( answerKey[end]!=ch1){
                if(k){
                    k-=1;
                }
                else{
                    while(begin<answerKey.length() && answerKey[begin]==ch1) begin+=1;
                    begin+=1;
                    if(begin>end){
                        end=begin;
                    }
                }
            }
            end+=1;
            ans=max(ans,end-begin);
        }

    }
    int maxConsecutiveAnswers(string answerKey, int k) {
        int ans=0;
       check(answerKey,k,ans,'T');
       check(answerKey,k,ans,'F');
       return ans;
    }
    int maxConsecutiveChar(string& answerKey, int k, char ch) {
        int n = answerKey.length();
        int ans = 0;
        for (int left = 0, right = 0, sum = 0; right < n; right++) {
            sum += answerKey[right] != ch;
            while (sum > k) {
                sum -= answerKey[left++] != ch;
            }
            ans = max(ans, right - left + 1);
        }
        return ans;
    }

    int maxConsecutiveAnswers_ans(string answerKey, int k) {
        return max(maxConsecutiveChar(answerKey, k, 'T'),
                   maxConsecutiveChar(answerKey, k, 'F'));
    }

};