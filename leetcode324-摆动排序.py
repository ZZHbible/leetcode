#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/6/28
# project = leetcode324-摆动排序
from typing import List
class Solution:
    # 垃圾写法
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        copy_nums = sorted(nums)
        _len = len(nums)
        if _len%2:
            min_nums = (copy_nums[0:(_len // 2)+1])
            max_nums = (copy_nums[(_len // 2)+1:])
        else:
            min_nums = (copy_nums[0:(_len // 2)])
            max_nums = (copy_nums[(_len // 2):])
        min_nums.reverse()
        max_nums.reverse()
        i, j, index, flag = 0, 0, 0, True
        while i < len(min_nums) :
            if flag:
                nums[index] = min_nums[i]
                i += 1
            else:
                nums[index] = max_nums[j]
                j += 1
            index += 1
            flag = not flag
        if j<len(max_nums):
            while index<_len and j<len(max_nums):
                nums[index]=max_nums[j]
                index+=1
                j+=1

    def wiggleSort1(self, nums: List[int]) -> None:
        n = len(nums)
        arr = sorted(nums)
        x = (n + 1) // 2
        j, k = x - 1, n - 1
        for i in range(0, n, 2):
            nums[i] = arr[j]
            if i + 1 < n:
                nums[i + 1] = arr[k]
            j -= 1
            k -= 1
    def wiggleSort2(self, nums: List[int]) -> None:
        bucket=[0]*5001
        for num in nums:
            bucket[num]+=1
        j=5000
        for i in range(1,len(nums),2):
            while bucket[j]==0:
                j-=1
            nums[i]=j
            bucket[j]-=1
        for i in range(0,len(nums),2):
            while bucket[j]==0:
                j-=1
            nums[i]=j
            bucket[j]-=1


solution=Solution()
nums=[1,4,3,4,1,2,1,3,1,3,2,3,3]
solution.wiggleSort(nums
)
print(nums)




