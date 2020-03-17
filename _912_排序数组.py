"""
给定一个整数数组 nums，将该数组升序排列。

示例 1：

输入：[5,2,3,1]
输出：[1,2,3,5]
示例 2：

输入：[5,1,1,2,0,0]
输出：[0,0,1,1,2,5]
 

提示：

1 <= A.length <= 10000
-50000 <= A[i] <= 50000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import random

class Solution(object):
        
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 冒泡排序
        # for i in range(len(nums)-1):
        #     for j in range(1, len(nums)-i):
        #         if nums[j] < nums[j-1]:
        #             tmp = nums[j]
        #             nums[j] = nums[j-1]
        #             nums[j-1] = tmp
        # return nums

        # 选择排序
        # for i in range(len(nums)-1):
        #     index = i
        #     for j in range(i+1, len(nums)):
        #         if nums[index] > nums[j]:
        #             index = j
        #     if index != i:
        #         tmp = nums[index]
        #         nums[index] = nums[i]
        #         nums[i] = tmp
        # return nums

        # 插入排序
        # for i in range(1, len(nums)):
        #     for j in range(1, i+1)[::-1]:
        #         if nums[j] < nums[j-1]:
        #             tmp = nums[j]
        #             nums[j] = nums[j-1]
        #             nums[j-1] = tmp
        # return nums
        self.quickSort(0, len(nums)-1, nums)
        return nums


    # 快速排序
    def quickSort(self, begin, end, nums):
        if begin >= end:
            return
        mid = self.partition(begin, end, nums)
        self.quickSort(begin, mid-1, nums)
        self.quickSort(mid+1, end, nums)

    def partition(self, begin, end, nums):

        index = begin + (end - begin) // 2
        self.swap(begin, index, nums)
        pivot = nums[begin]
        while begin < end:
            while begin < end:
                if nums[end] > pivot:
                    end -= 1
                else:
                    nums[begin] = nums[end]
                    begin += 1
                    break
            while begin < end:
                if nums[begin] < pivot:
                    begin += 1
                else:
                    nums[end] = nums[begin]
                    end -= 1
                    break
        nums[begin] = pivot
        return begin

    def swap(self, i, j, nums):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
        

if __name__ == "__main__":
    nums = [5,2,3,1]
    # nums = [5,1,1,2,0,0]
    res = Solution().sortArray(nums)
    print(res)
