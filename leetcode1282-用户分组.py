class Solution:
    # numpy 排序
    from typing import List
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        import numpy as np
        group=np.array(groupSizes)
        arg_group=group.argsort()
        ans,i=[],0
        add=[]
        while i<len(arg_group):
            add.append(int(arg_group[i]))
            if group[arg_group[i]] == len(add):
                ans.append(add)
                add=[]
            i+=1
        return ans
    # hash_map
    def groupThePeople_ans(self, groupSizes: List[int]) -> List[List[int]]:
        from collections import defaultdict
        dic=defaultdict(list)
        for index,num in enumerate(groupSizes):
            dic[num].append(index)
        ans=[]
        for key,l in dic.items():
            index=key
            while index<=len(l):
                ans.append(l[index-key:index])
                index+=key
        return ans
solution=Solution()
solution.groupThePeople_ans([3,3,3,3,3,1,3])

