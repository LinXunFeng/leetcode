"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

注意：你不能在买入股票前卖出股票。


示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
解题思路
1. 数组（一次遍历）：
遍历一一遍，以当前遍历到的值为卖出的值
在这个过程中记录最小值，并计算最大利润的值


2. 动态规划：
minPrice: i天前的最小值
dp[i]： 前i天里卖出后的最大利润
dp[0] = 0： 第0个卖出，没有买入，所以可以确定初始值dp[0]是0
dp[i] 与 dp[i-1] 的转换方程： dp[i] = max(dp[i-1], price[i]-minPrice)


3. 动态规划：
第i天买，第j天卖的利润是
第i~j天内，所有相邻两天股价差的和
如：第1天买入，第4天卖出（从0天开始计算）
delta = 6-1 = 5
delta = (5-1)+(3-5)+(6-3) = 6-1 = 5

[7,1,5,3,6,4]
算出所有相邻两天的股价差
---------------------------
0~1 | 1~2 | 2~3 | 3~4 | 4~5
---------------------------
-6  |  4  | -2  | 3   | -2
---------------------------

将问题转化为 => 求【最大子数组和】的问题，即【最大连续子序列和】的问题
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        数组（一次遍历）
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if prices is None or n == 0:
          return 0
        maxProfit = 0 # 最在利润值
        minPrice = prices[0] # 最小值
        for i in range(1, n):
          if prices[i] > minPrice:
            delta = prices[i] - minPrice
            if delta > maxProfit:
              maxProfit = delta
          else:
            minPrice = prices[i]
        return maxProfit

    def maxProfit2(self, prices):
        """
        动态规划
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if prices is None or n == 0:
          return 0
        
        dp = [0] * n # 创建化 dp[0] 为0
        minPrice = prices[0]

        for i in range(1, n):
          minPrice = min(minPrice, prices[i])
          # dp[i] 为前i天的最大利润值
          dp[i] = max(dp[i-1], prices[i]-minPrice) # i-1天前的最大利润 与 第i天的最大利润 相比，取最大值
        
        return dp[-1]
      
    def maxProfit3(self, prices):
        """
        动态规划（求：最大连续子序列和）
        :type prices: List[int]
        :rtype: int
        """
        def maxSubList(deltaList, right):
          """
          求最大子数组和
          """
          res = deltaList[0]
          for i in range(1, right):
            if deltaList[i-1] > 0:
              deltaList[i] += deltaList[i-1]
            res = max(res, deltaList[i])
          return res

        n = len(prices)
        if prices is None or n < 2:
          return 0
        
        # 计算相邻两天的差值列表
        size = n-1
        deltaList = []
        for i in range(size):
          deltaList.append(prices[i+1]-prices[i])
        
        # 求最大连续子序列和
        res = maxSubList(deltaList, size)
        return res if res > 0 else 0


if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    prices = [1]
    # res = Solution().maxProfit(prices)
    # res = Solution().maxProfit2(prices)
    res = Solution().maxProfit3(prices)
    print(res)
