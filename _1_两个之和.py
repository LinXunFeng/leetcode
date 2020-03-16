class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_dict = {}
        
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in index_dict:
                return [index_dict[tmp], i]
            index_dict[nums[i]] = i

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))