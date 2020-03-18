"""
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
示例 2:

输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false
示例 3:

输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false
"""
from TreeNode import TreeHander

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # 递规判断每个节点是否相同
        if p is None or q is None:
            return p is None and q is None
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # 遍历后判断是否相同
    #     if p is None or q is None:
    #         return p is None and q is None
    #     pOrderList = []
    #     qOrderList = []
    #     self.preOrder(pOrderList, p)
    #     self.preOrder(qOrderList, q)
    #     return pOrderList == qOrderList

    # def preOrder(self, list, root):
    #     if root is None:
    #         list.append(-1)
    #         return
    #     list.append(root.val)
    #     self.preOrder(list, root.left)
    #     self.preOrder(list, root.right)
        

if __name__ == "__main__":
    p = [1,2,3,4]
    q = [1,2,3]
    pHead = TreeHander.reConsTreeForLevel(p)
    qHead = TreeHander.reConsTreeForLevel(q)
    res = Solution().isSameTree(pHead, qHead)
    print(res)