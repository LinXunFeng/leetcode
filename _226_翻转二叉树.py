"""
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""

from TreeNode import TreeNode, TreeHander

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

if __name__ == "__main__":
    level = [4,2,7,1,3,6,9]
    head = TreeHander.reConsTreeForLevel(level)
    print('翻转前：')
    TreeHander.levelOrderTreeNode(head)
    res = Solution().invertTree(head)
    print('\n翻转后：')
    TreeHander.levelOrderTreeNode(res)
    print('')
    
