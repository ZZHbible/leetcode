#!/usr/bin/env python
# author = 'ZZH'
# time = 2021/11/17
# project = leetcode318-最大单词长度乘积

class Solution:
    def maxProduct(self, words) -> int:
        w_dict={} #用一个哈希表映射 word:len(word) 方便查找
        for i in words:
            w_dict[i]=len(i)
        words.sort(key=lambda a:len(a),reverse=True)
        ret=0
        # 遍历，后面的word中的ch在该word中出现就break，没出现就将ret=max(ret,w_dict[val]*w_dict[words[j]])
        for i,val in enumerate(words):
            for j in range(i+1,len(words)):
                flag=True
                for ch in words[j]:
                    if ch in val:
                        flag=not flag
                        break
                if flag:
                    ret=max(ret,w_dict[val]*w_dict[words[j]])
                    break #减枝，因为再往后遍历，len(word)都会比len(words[j])短
        return ret

S=Solution()
words= ["abcw","baz","foo","bar","xtfn","abcdef"]
print(S.maxProduct(words))
