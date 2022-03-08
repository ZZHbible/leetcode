from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        len_=len(s)
        left_Candle,right_Candle=[-1]*len_,[-1]*len_
        num=[0]*len_
        for i in range(len_):
            if s[i]=='|':
                j=i
                while(j>=0 and right_Candle[j]==-1):
                    right_Candle[j]=i
                    j-=1
        for i in range(len_-1,-1,-1):

            if s[i]=='|':
                j=i
                while(j<len_ and left_Candle[j]==-1):
                    left_Candle[j]=i
                    j+=1
        flag=False
        temp=0
        last=0
        for i in range(len_):
            if s[i]=='|':
                if flag:
                    num[i]=last+temp
                    last=num[i]
                    temp=0
                else:
                    flag=True
            else:
                if flag:
                    temp+=1
        ans=[]
        for query in queries:
            left,right=right_Candle[query[0]],left_Candle[query[1]]
            if left==-1 or right==-1 or left>=right:
                ans.append(0)
            else:
                ans.append(num[right]-num[left])
        return ans


