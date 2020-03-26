"""
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
说明:

如果你可以运用递归和迭代两种方法解决这个问题，会很加分。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/symmetric-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from TreeNode import TreeHander

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if root.left is None and root.right is not None:
            return False
        if root.left is not None and root.right is None:
            return False
        if root.left.val != root.right.val:
            return False
        return self.isSymmetric(root.left) and self.isSymmetric(root.right)
        


if __name__ == "__main__":
    p = [1,2,2,3,4,4,3]
    pHead = TreeHander.reConsTreeForLevel(p)
    res = Solution().isSymmetric(pHead)
    print(res)