from typing import List


class Solution:
    # use numpy
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        num=[ abs(num-x) for num in arr]
        import numpy as np
        num=np.array(num)
        arg_index=np.argsort(num,kind='stable')
        ans=[]
        for i in range(k):
            ans.append(arr[arg_index[i]])
        return sorted(ans)

