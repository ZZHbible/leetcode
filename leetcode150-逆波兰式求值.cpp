class Solution {
public:
    bool is_op(string str){
        if(str=="/" || str=="*" || str=="+"|| str=="-") return true;
        return false;
    }

    int evalRPN(vector<string>& tokens) { // 2+1*3*5
        vector<int> num;
        for(string str:tokens){
            if(is_op(str)){
                int num_2=num.back();
                num.pop_back();
                int num_1=num.back();
                num.pop_back();
                if(str=="/")num.emplace_back(num_1/num_2);
                else if (str=="*")num.emplace_back(num_1*num_2);
                else if (str=="+")num.emplace_back(num_1+num_2);
                else if (str=="-")num.emplace_back(num_1-num_2);
            }
            else num.emplace_back(stoi(str));
        }
        return num[0];

    }
};