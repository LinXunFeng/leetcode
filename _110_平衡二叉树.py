"""
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/balanced-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from TreeNode import TreeNode, TreeHander

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        delta = left_height - right_height 
        # 判断左右子树是否平衡
        if delta > 1 or delta < -1:
            return False
        # 递归判断左右子树的左右子树是否平衡
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, node):
        if node is None:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return (left_height if left_height > right_height else right_height) + 1

if __name__ == "__main__":
    tree = [3,9,20,None,None,15,7]
    root = TreeHander.reConsTreeForLevel(tree)
    isBlanced = Solution().isBalanced(root)
    print(isBlanced)