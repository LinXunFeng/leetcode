"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
解题：
s为字符串数组
pi是s[i]字符上一次出现的位置
li是以s[i-1]字符结尾的最长不重复子串的开始索引（最左索引）

li会出现以下三种情况：

下标  0        pi    li   i-1 i
元素           D           A  D

下标  0   li   pi         i-1 i
元素           D           A  D

下标  0      li/pi        i-1 i
元素           D           A  D

第一种情况：    i的最长子串是[li, i]
第二/三种情况： i的最长子串是[pi, i]

"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
          return 0
        arr = list(s)
        preIndexDict = {} # 保存第个字符上一次出现的位置
        preIndexDict[arr[0]] = 0
        li = 0 # 以s[i-1]字符结尾的最长不重复子串的开始索引（最左索引）
        maxLen = 1 # 最长无重复字符的长度 (i 从 1 开始)
        for i in range(1, len(arr)):
          pi = preIndexDict.get(arr[i], -1) # i位置字符上一次出现的位置 (如果pi为None，则 i的最长不重复子串为 arr[li, i]，pi给个最左边的下标就好，如-1)
          
          # if li > pi: # i的最长不重复子串为arr[li, i]，li不需要更新
          if li <= pi: # i的最长不重复子串为arr[pi+1, i]，更新 li
            li = pi + 1

          preIndexDict[arr[i]] = i # 存储当前字符出现的位置
          maxLen = max(i-li+1, maxLen) # 求最长不重复子串的长度

        return maxLen

    def lengthOfLongestSubstring2(self, s):
        """
        如果给定的字符串s是只包含ascii码表中的值，可以用长度为128的数组进行优化
        ASCII码转换为int：ord('A') 65
        int转为ASCII码：chr(65) 'A'
        """
        if len(s) == 0:
          return 0
        arr = list(s)
        preIndexArr = [-1] * 128 # 保存第个字符上一次出现的位置 （初始化了128个-1）
        preIndexArr[ord(arr[0])] = 0
        li = 0 # 以s[i-1]字符结尾的最长不重复子串的开始索引（最左索引）
        maxLen = 1 # 最长无重复字符的长度 (i 从 1 开始)
        for i in range(1, len(arr)):
          pi = preIndexArr[ord(arr[i])] # i位置字符上一次出现的位置 (如果pi为None，则 i的最长不重复子串为 arr[li, i]，pi给个最左边的下标就好，如-1)
          
          # if li > pi: # i的最长不重复子串为arr[li, i]，li不需要更新
          if li <= pi: # i的最长不重复子串为arr[pi+1, i]，更新 li
            li = pi + 1

          preIndexArr[ord(arr[i])] = i # 存储当前字符出现的位置
          maxLen = max(i-li+1, maxLen) # 求最长不重复子串的长度

        return maxLen


if __name__ == "__main__":
    str = "abcabcbb"
    # res = Solution().lengthOfLongestSubstring(str)
    res = Solution().lengthOfLongestSubstring2(str)
    print(res)
