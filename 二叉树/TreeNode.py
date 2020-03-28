# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TreeHander(object):
    @classmethod
    def reConsTreeForPre(cls, pre, mid):
        """
        重构二叉树(前+中)
        """
        # 判断前、中序遍历是否为空
        if pre is None or mid is None:
            return
        if (len(pre) or len(mid)) == 0:
            return
        # 前序遍历的第一个元素即为根元素
        # 找出根元素在中序遍历中的索引
        # 知道root的索引就可以知道各左、右子树的节点总数
        root_index = mid.index(pre[0])
        # 实例化根节点
        root = TreeNode(pre[0])
        # 重构左右子树
        root.left = cls.reConsTreeForPre(pre[1:root_index+1], mid[:root_index])
        root.right = cls.reConsTreeForPre(pre[root_index+1:], mid[root_index+1:])
        return root

    @classmethod
    def reConsTreeForEnd(cls, end, mid):
        """
        重构二叉树(后+中)
        """
        if end is None or mid is None:
            return
        if (len(end) or len(mid)) == 0:
            return
        root_index = mid.index(end[-1])
        root = TreeNode(end[-1])
        root.left = cls.reConsTreeForEnd(end[:root_index], mid[:root_index])
        root.right = cls.reConsTreeForEnd(end[root_index:len(end)-1], mid[root_index+1:])
        return root

    @classmethod
    def reConsTreeForLevel(cls, level_list):
        """
        重构二叉树(层序遍历)
        """
        if level_list is None or len(level_list) == 0:
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
    def preOrderTreeNode(cls, root):
        """
        前序遍历
        """
        if root is None:
            return
        print(root.val,  end=" ")
        cls.preOrderTreeNode(root.left)
        cls.preOrderTreeNode(root.right)
    
    @classmethod
    def preOrderTreeNode2(cls, root):
        """
        前序遍历(非递规)
        """
        if root is None:
            return
        stack = []
        while stack or root:
            while root:
                print(root.val, end=" ")
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right

    @classmethod
    def midOrderTreeNode(cls, root):
        """
        中序遍历
        """
        if root is None:
            return
        cls.midOrderTreeNode(root.left)
        print(root.val, end=" ")
        cls.midOrderTreeNode(root.right)

    @classmethod
    def midOrderTreeNode2(cls, root):
        """
        中序遍历(非递规)
        """
        if root is None:
            return
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            print(root.val, end=" ")
            root = root.right

    @classmethod
    def postOrderTreeNode(cls, root):
        """
        后序遍历
        """
        if root is None:
            return
        cls.postOrderTreeNode(root.left)
        cls.postOrderTreeNode(root.right)
        print(root.val,  end=" ")

    @classmethod
    def postOrderTreeNode2(cls, root):
        """
        后序遍历(非递规)
        """
        if root is None:
            return
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left if root.left else root.right
            root = stack.pop() # 左子树或右子树遍历完了，取父节点
            print(root.val, end=" ")
            if stack and stack[-1].left == root: # 父节点是祖父节点的左子节点
                root = stack[-1].right # 开始遍历右子树
            else:
                root = None


    @classmethod
    def levelOrderTreeNode(cls, root):
        if root is None:
            return
        stack = [root]
        while stack:
            tmpStack = []
            for node in stack:
                print(node.val, end=" ")
                if node.left is not None:
                    tmpStack.append(node.left)
                if node.right is not None:
                    tmpStack.append(node.right)
            
            stack = tmpStack
            tmpStack = []




if __name__ == "__main__":
    # pre = [4, 2, 1, 3, 5, 7, 6]
    # mid = [1, 2, 3, 4, 5, 6, 7]
    # head = TreeHander.reConsTreeForPre(pre, mid)
    # TreeHander.postOrderTreeNode(head)

    # end = [1, 3, 2, 6, 7, 5, 4]
    # mid = [1, 2, 3, 4, 5, 6, 7]
    # head = TreeHander.reConsTreeForEnd(end, mid)
    # TreeHander.midOrderTreeNode(head)

    level = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    head = TreeHander.reConsTreeForLevel(level)
    # TreeHander.preOrderTreeNode(head)
    # TreeHander.preOrderTreeNode2(head)
    # TreeHander.midOrderTreeNode(head)
    # TreeHander.midOrderTreeNode2(head)
    # TreeHander.postOrderTreeNode(head)
    TreeHander.postOrderTreeNode2(head)
    # TreeHander.levelOrderTreeNode(head)
