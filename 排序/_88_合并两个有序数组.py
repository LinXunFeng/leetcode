"""
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 num1 成为一个有序数组。

 

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
 

示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p = m + n - 1
        m = m - 1
        n = n - 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]: # 当前 nums1[m] 为最大值 
                nums1[p] = nums1[m]
                m -= 1
                p -= 1
            else:
                nums1[p] = nums2[n]
                n -= 1
                p -= 1
        # nums2可能还没全部加入到 nums1
        while n >= 0:
            nums1[p] = nums2[n]
            n -= 1
            p -= 1


if __name__ == "__main__":
    nums1 =[1,2,3,0,0,0]
    m = 3
    nums2 =[2,5,6]
    n = 3
    Solution().merge(nums1, m, nums2, n)
    print(nums1)