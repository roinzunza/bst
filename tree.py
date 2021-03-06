from node import Node


class Tree(object):

    def insert_bst(self, root: Node, data: int):
        # root passed will check if its empty (passed from left or right) and insert data to node

        if root is None:
            root = Node(data)
            return root
        # binary search tree is not empty, so we will insert it into the tree
        # if data is less than the root go to the left of the root and call recursively
        if data < root.data:
            root.left = self.insert_bst(root.left, data)
        # if data is greater than the root go to the right of the root and call recursively
        elif data > root.data:
            root.right = self.insert_bst(root.right, data)
        return root

    def depth_first(self, root: Node):
        if root.left is not None:
            self.depth_first(root.left)
        print(root.data, end=' ')
        if root.right is not None:
            self.depth_first(root.right)

    def tree_depth(self, node: Node):
        if not node:
            return 0
        else:
            return max(self.tree_depth(node.left), self.tree_depth(node.right)) + 1

    def print_tree(self, node: Node):
        if not node:
            return node

        self.print_tree(node.left)
        print('{}'.format(node.data), end=' ')
        self.print_tree(node.right)

    def print_leaves(self, node: Node):
        if not node:
            return node

        if not node.left and not node.right:
            print(node.data, end=' ')
            return

        if node.left:
            self.print_leaves(node.left)

        if node.right:
            self.print_leaves(node.right)

    def in_order(self, node: Node):
        if not node:
            return node

        self.in_order(node.left)
        print(node.data, end=' ')
        self.in_order(node.right)

    def pre_order(self, node: Node):
        if not node:
            return node

        print(node.data, end=' ')
        self.pre_order(node.left)
        self.pre_order(node.right)

    def post_order(self, node: Node):
        if not node:
            return node

        self.post_order(node.left)
        self.post_order(node.right)
        print(node.data, end=' ')

    def make_tree(self, elements: list):
        root_node = Node(1)
        for element in elements:
            self.insert_bst(root_node, element)

        return root_node
