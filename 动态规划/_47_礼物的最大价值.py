"""
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

示例 1:

输入: 
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
 

提示：

0 < grid.length <= 200
0 < grid[0].length <= 200

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
[1,3,1]
[1,5,1]
[4,2,1]


dp | 0  1   2
---|-----------
0  | 1  4   5
1  | 2  9   10
2  | 6  11  12

先求出第0行一事行的值，和第0列一整列的值
再一行一行求最大值

"""

class Solution(object):
    def maxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None or len(grid) == 0:
          return 0
        rows = len(grid) # 行数
        cols = len(grid[0]) # 列数
        dp = [[0] * cols for i in range(rows)] # 初始化 rows * cols 的二维数组
        dp[0][0] = grid[0][0]
        # 第0行 与 第0列 上的最大值都是当前值与前一个最大值相加所得
        for col in range(1, cols):
          dp[0][col] = dp[0][col-1] + grid[0][col]
        for row in range(1, rows):
          dp[row][0] = dp[row-1][0] + grid[row][0]
        
        for row in range(1, rows):
          for col in range(1, cols):
            dp[row][col] = max(dp[row-1][col], dp[row][col-1]) + grid[row][col]

        return dp[rows-1][cols-1]

    def maxValue2(self, grid):
        """
        一维DP
        dp存放的是上一行的所有最大值
        """
        if grid is None or len(grid) == 0:
          return 0
        rows = len(grid)
        cols = len(grid[0])
        dp = [0] * (cols+1)
        for row in range(rows):
          for col in range(cols):
            dp[col+1] = max(dp[col], dp[col+1]) + grid[row][col]
        return dp[-1] 


if __name__ == "__main__":
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    res = Solution().maxValue2(grid)
    print(res)