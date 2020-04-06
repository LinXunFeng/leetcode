"""
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
 

示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2：

输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/edit-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
           0 1 2
         j r o s
    ------------
    | dp 0 1 2 3
  i | 0  0 1 2 3
0 h | 1  1 x x x
1 o | 2  2 x x x
2 r | 3  3 x x x
3 s | 4  4 x x x
4 e | 5  5 x x x

len1 = len(word1)
len2 = len(word1)
dp：大小为 len1+1, len2+1 的二维数组
dp[i][j]：从 word1[0, i) 转换成 word2[0, j)的最少操作数
          word1[0, i)：由word1的前i个字符组成的子串
          word2[0, j)：由word1的前i个字符组成的子串
初始值：dp[i][0] 与 dp[0][j] 上的值都是可通过前一个插入一个即可得到，最初的值为空字符串
最终值：dp[len1][len2]，即word1[0, len1)转换成word2[0, len2)的最少操作数
状态转移方程：有四种情况
    1. 由 word1[0, i) 删除最后一个字符得到 word2[0, j)，即 word1[0, i-1) 转换成 word2[0, j)
        从当前列的上一行得到结果  top
        dp[i][j] = 1 + dp[i-1][j]  

    2. 由 word1[0, i) 转换成 word2[0, j-1) 后，插入一个字符得到 word2[0, j)
        从当前行的前一个得到结果  left
        dp[i][j] = dp[i][j-1] + 1

    3. 根据 word1[0, i) 与word2[0, j) 最后一个字符相同与否，有两个情况
        从上一行的前一个得到结果  leftTop
      3.1 word1[i-1] != word2[j-1]
          先 word1[0, i-1) 转换成 word2[0, j-1) 后，再将 word1[i-1] 替换为 word2[j-1] 即可
          dp[i][j] = dp[i-1][j-1] + 1

      3.2 word1[i-1] == word2[j-1]
          直接 word1[0, i-1) 转换成 word2[0, j-1) 后，不需要再做其它操作
          dp[i][j] = dp[i-1][j-1]

"""
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        wl1 = list(word1)
        wl2 = list(word2)
        lenWl1 = len(wl1)
        lenWl2 = len(wl2)
        dp = [[0] * (lenWl2+1) for i in range(lenWl1+1)] # 大小为 lenWl1+1, lenWl2+1 的二维数组
        for i in range(1, lenWl1+1): # 初始化第0列的所有值
          dp[i][0] = i
        for j in range(1, lenWl2+1): # 初始化第0行的所有值
          dp[0][j] = j
        print(dp)
        # 补充其它行的值
        for i in range(1, lenWl1+1):
          for j in range(1, lenWl2+1):
            top = dp[i-1][j] + 1
            left = dp[i][j-1] + 1
            leftTop = dp[i-1][j-1]
            if wl1[i-1] != wl2[j-1]:
              leftTop += 1
            dp[i][j] = min(min(top, left), leftTop)

        return dp[lenWl1][lenWl2] # 返回最终的结果


if __name__ == "__main__":
    word1 = "horse"
    word2 = "ros"
    res = Solution().minDistance(word1, word2)
    print(res)
