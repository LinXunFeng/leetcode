"""
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from TreeNode import TreeNode, TreeHander

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        stack = [root]
        result = []

        while len(stack):
            tmp_stack = []
            tmp_arr = []
            for node in stack:
                tmp_arr.append(node.val)
                if node.left != None:
                    tmp_stack.append(node.left)
                if node.right != None:
                    tmp_stack.append(node.right)
                
            stack = tmp_stack
            result.append(tmp_arr)
        
        return result[::-1]


if __name__ == "__main__":
    arr = [3,9,20,None,None,15,7]
    root = TreeHander.reConsTreeForLevel(arr)

    value = Solution().levelOrderBottom(root)
    print(value)
