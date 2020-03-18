# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TreeHander(object):
    @classmethod
    def reConsTree_for_pre(cls, pre, mid):
        """
        重构二叉树(前+中)
        """
        # 判断前、中序遍历是否为空
        if (len(pre) or len(mid)) == 0:
            return
        # 前序遍历的第一个元素即为根元素
        # 找出根元素在中序遍历中的索引
        mid_index = mid.index(pre[0])
        # 实例化根节点
        tree = TreeNode(pre[0])
        # 重构左右子树
        tree.left = cls.reConsTree_for_pre(pre[1:mid_index+1], mid[:mid_index])
        tree.right = cls.reConsTree_for_pre(pre[mid_index+1:], mid[mid_index+1:])
        return tree


    @classmethod
    def reConsTree_for_level(cls, level_list):
        """
        重构二叉树(层序遍历)
        """
        if len(level_list) == 0:
            return
        node_list = []
        for i in level_list:
            node_list.append(TreeNode(i))

        node_list_len = len(node_list)
        for i in range(node_list_len):
            left_index = 2*i+1
            right_index = 2*i+2
            if left_index < node_list_len and level_list[left_index] is not None:
                node_list[i].left = node_list[left_index]
            if right_index < node_list_len and level_list[right_index] is not None:
                node_list[i].right = node_list[right_index]
        
        return node_list[0]


    @classmethod
    def traversalTreeNode(cls, tree):
        """
        后序遍历
        """
        if tree is None:
            return
        cls.traversalTreeNode(tree.left)
        cls.traversalTreeNode(tree.right)
        print(tree.val)


if __name__ == "__main__":
    # pre = [4, 2, 1, 3, 5, 7, 6]
    # mid = [1, 2, 3, 4, 5, 6, 7]
    # head = TreeHander.reConsTree_for_pre(pre, mid)
    # TreeHander.traversalTreeNode(head)

    level = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    head = TreeHander.reConsTree_for_level(level)
    TreeHander.traversalTreeNode(head)
