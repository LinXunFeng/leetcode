"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
动态规划
  j  b a b a d
i dp 0 1 2 3 4
b 0
a 1
b 2
a 3
d 4

s为目标字符串，n为其长度
dp：大小为 n*n 的二维数组，存储 True、False
dp[i][j]：s[i, j], s从下标i到j的子串是否为回文串
状态转移方程：（两种情况）
    s[i, j]的长度 j-i+1 大不大于 2
    1. 长度 <= 2
        判断左下标与右下标对应的字符是否相同，若相同则为回文串
        dp[i][j] = s[i] == s[j]
    2. 长度 > 2
        如果s[i+1, j-1]是回文串，并且 s[i]==s[j]，则s[i, j]是回文串
        dp[i][j] = dp[i+1, j-1] && s[i] == s[j]
        注意：当前值，需要左下角的值来推导！！

从下到上，从左到右计算出 bp 的所有值

时间复杂度：O(n^2)
空间复杂度：O(n^2)
====================================================================

扩展中心法

从4开始，向左右扩展，得到的永远是奇数位的结果
        i
     <--|-->
0 1 2 3 4 5
a b b a b a

从1和2的间隙开始，向左右扩展，可得到偶数位的结果
   i
<--|-->
0 1 2 3 4 5
a b b a b a

假设字符串长度为 n，则一共有 n + (n-1) = 2n-1 个扩展中心
时间复杂度：O(n^2)
空间复杂度：O(1)
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        动态规划
        :type s: str
        :rtype: str
        """
        if s is None or len(s) <= 1:
          return s
        cs = list(s)
        n = len(cs)
        maxLen = 1 # 最长回文子串的长度（单字符也算是回文子串）
        begin = 0 # 最长回文子串的开始索引
        dp = [[False] * n for i in range(n)]
        for i in range(n)[::-1]: # 从下到上
          for j in range(i, n): # 从左到右 (j>=i才有意义)
            dp[i][j] = s[i] == s[j] # 不管长度大不大于2，这个都必须满足
            length = j-i+1
            if length > 2:
              dp[i][j] = dp[i][j] and dp[i+1][j-1]
            if dp[i][j] and length > maxLen: # 说明 cs[i, j] 是回文子串
              maxLen = length
              begin = i
        return ''.join(cs[begin:begin+maxLen])
              
    def longestPalindrome2(self, s):
        """
        扩展中心法
        :type s: str
        :rtype: str
        """
        def palindromeLength(cs, l, r):
          """
          获取最长回文子串的长度
          cs: 原字符串列表
          l: 左下标
          r: 右下标
          返回元祖：(int 回文子串的长度, int 回文子串的起始下标)
          """
          while l>=0 and r<len(cs) and s[l]==s[r]:
            l -= 1
            r += 1
          # 退出循环时，l与r对应的字符不相等
          return (r-l-1, l+1)

        if s is None or len(s) <= 1:
          return s
        cs = list(s)
        n = len(cs)
        maxLen = 1 # 最长回文子串的长度（单字符也算是回文子串）
        begin = 0 # 最长回文子串的开始索引
        for i in range(1, n-1): # 从第1个到倒数第2个
          (len1, i1) = palindromeLength(cs, i-1, i)   # 以左边间隙为中心，向左右扩展
          (len2, i2) = palindromeLength(cs, i-1, i+1) # 以当前下标为中心，向左右扩展
          length = max(len1, len2)
          if length > maxLen:
            maxLen = length
            begin = i1 if len1>len2 else i2
         
        # 处理倒数第一个左边间隙为扩展中心（最大回文子串的长度 只能是0或2）
        if cs[-1]==cs[-2] and maxLen < 2: # 如果成立，则cs[-1, -2]为最长回文子串
          begin = n-2
          maxLen = 2
        return ''.join(cs[begin:begin+maxLen])


if __name__ == "__main__":
    s = "babad"
    s = "cbbd"
    res = Solution().longestPalindrome(s)
    print(res)
