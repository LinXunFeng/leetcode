"""
二叉搜索树中的两个节点被错误地交换。

请在不改变其结构的情况下，恢复这棵树。

示例 1:

输入: [1,3,null,null,2]

   1
  /
 3
  \
   2

输出: [3,1,null,null,2]

   3
  /
 1
  \
   2
示例 2:

输入: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

输出: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/recover-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
二叉搜索树的特点：
  - 左子树上的所有节点比根节点小，右子树上的所有节点比根节点大
  - 中序遍历的结果是升序


    28                 22                 
   / \                / \
  18  37             18  37           
 / \   \      =>    / \   \
11 22  44          11 28  44
 \     / \          \     / \
 17   42 62         17   42 62

22 与 28 进行了交换

中序遍历：
  11, 17, 18, 22, 28, 37, 42, 44, 62
  11, 17, 18, 28, 22, 37, 42, 44, 62
              ——————


    28                 28                 
   / \                / \
  18  37             44  37           
 / \   \      =>    / \   \
11 22  44          11 22  18
 \     / \          \     / \
 17   42 62         17   42 62

18 与 44 进行了交换

中序遍历：
  11, 17, 18, 22, 28, 37, 42, 44, 62
  11, 17, 44, 22, 28, 37, 42, 18, 62
          ——————          ——————

如果错误节点相邻，则只有一个逆序对
如果错误节点不相邻，则只有两个逆序对

将上述两种情况总结为一个：
  第1个错误节点：第1个逆序对中的较大节点
  第2个错误节点：最后1个逆序对中的较小节点

时间复杂度：O(n)  前序遍历
空间复杂度：O(h)  最坏：O(n)
"""

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.prev = None # 记录遍历的上一个节点
        self.first = None # 第1个错误节点
        self.second = None # 第2个错误节点
        # 找出两个错误节点
        self.findWrongNode(root)
        # 交换两个错误节点的值
        self.first.val, self.second.val = self.second.val, self.first.val
    
    def findWrongNode(self, root):
      """
      找出错误节点，并赋值给 self.first 和 self.second
      """
      if root is None: return
      # 使用中序遍历
      self.findWrongNode(root.left)

      if self.prev is not None and self.prev.val > root.val: # prev：上一个节点
        # 出现逆序对
        self.second = root # 第2个错误节点：最后1个逆序对中的较小节点
        if self.first is not None: return # first不为空，则当前找到的是第2个逆序对
        self.first = self.prev
      
      self.prev = root

      self.findWrongNode(root.right)
