from typing import List

'''
    煎饼排序，反复反转前k个值，使最终有序
'''


class Solution:
    # 找到未排序的最大值下标，移到第一位，再移到最后，完成单个数的排序
    def pancakeSort(self, arr: List[int]) -> List[int]:
        len_ = len(arr) - 1
        ans = []
        while len_ > 0:
            while len_ > 0 and arr[len_] == len_ + 1: len_ -= 1  # 剪枝
            if len_ < 1: break
            index_ = arr.index(len_ + 1)

            def exchange(left, right):
                while left < right:
                    arr[left], arr[right] = arr[right], arr[left]
                    left += 1
                    right -= 1

            if index_ == 0:
                ans.append(len_ + 1)
                exchange(0, len_)
            else:
                ans.append(index_ + 1)
                exchange(0, index_)
        return ans


solution = Solution()
print(solution.pancakeSort([1, 2, 3]))
