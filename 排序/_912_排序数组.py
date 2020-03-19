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
        # 【针对 小规模数据 或 基本有序 时十分高效】
        # for i in range(1, len(nums)):
        #     for j in range(1, i+1)[::-1]:
        #         if nums[j] < nums[j-1]:
        #             tmp = nums[j]
        #             nums[j] = nums[j-1]
        #             nums[j-1] = tmp
        # return nums

        # 快速排序
        # self.quickSort(0, len(nums)-1, nums)
        # return nums

        # 堆排序
        # (选择排序的升级版)
        # self.heapSort(nums)
        # return nums

        # 希尔排序
        # (插入排序的升级版)
        # 以增量组成小组，对该小组进行插入排序，形成部分有序
        # 每次都缩小增量，重复上一步的操作
        # 最后一次排序时，增量为1，此时的数组已经达到基本有序
        length = len(nums)
        gap = length // 2
        while gap >= 1:
            for i in range(gap, length):
                j = i
                while j>=gap and nums[j-gap]>nums[j]:
                    nums[j],nums[j-gap] = nums[j-gap],nums[j]
                    j-= gap
            gap = gap // 2
        return nums



    # 快速排序
    def quickSort(self, begin, end, nums):
        if begin >= end:
            return
        mid = self.partition(begin, end, nums)
        self.quickSort(begin, mid-1, nums)
        self.quickSort(mid+1, end, nums)

    def partition(self, begin, end, nums):
        """
        分区
        """
        # 将小于轴点的元素放在左边，大于轴点元素放在右边
        # 遍历完成后，begin与end重合，即为轴点索引
        # 给轴点元素赋值，并返回轴点的索引
        index = begin + (end - begin) // 2 # index最好采用随机值，保证左右分区平衡
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

    # 堆排序
    def heapSort(self, nums):
        nums_length = len(nums)
        for i in range(nums_length-1):
            # 将元素建堆
            self.heapify(nums, nums_length-i)
            # 将堆顶元素与最后元素交换 => 最后一位即为最大值
            last = nums_length-1-i
            self.swap(last, 0, nums)

    def heapify(self, nums, n):
        """
        原地建堆(自下而上的下滤)
        """
        # 从下向上不断跟父节点比较，比父元素大就交换
        for i in range(0, n)[::-1]:
            current_index = i
            node = nums[i]
            parent_index = (current_index-1)//2
            while parent_index >=0 and nums[parent_index] < node:
                nums[current_index] = nums[parent_index]
                current_index = parent_index
                parent_index = (current_index-1)//2

            if current_index != i:
                nums[current_index] = node


    def swap(self, i, j, nums):
        # tmp = nums[i]
        # nums[i] = nums[j]
        # nums[j] = tmp
        nums[i], nums[j] = nums[j], nums[i];
        
        

if __name__ == "__main__":
    # nums = [1, 2, 3, 4, 5]
    nums = [5,2,3,1]
    # nums = [5,1,1,2,0,0]
    res = Solution().sortArray(nums)
    print(res)
