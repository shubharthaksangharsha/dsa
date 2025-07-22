class Node:
    """
    Represents a node in a binary tree.
    """

    def __init__(self, data=None, left=None, right=None):
        """
        Initializes a Node object.

        Args:
            data: The data to be stored in the node.
        """
        self.data = data
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.data + " " + self.left + " " + self.right)


class BinaryTree:
    """
    Represents a binary tree.
    """

    def __init__(self, root_data=None, left=None, right=None):
        """
        Initializes a BinaryTree object.

        Args:
            root_data: The data for the root node (optional). If None, the tree is empty.
        """
        if root_data is not None:
          self.root = Node(root_data, left, right)
        else:
          self.root = None
    
    def inorder_traversal(self, node):
        if self.root is None:
            return
        self.inorder_traversal(node.left)
        print(node.data)
        self.inorder_traversal(node.right)
    
    def preorder_traversal(self, node):
        if self.root is None:
            return
        print(node.data)
        self.preorder_traversal(node.left)
        self.preorder_traversal(node.right)
    
    def postorder_traversal(self, node):
        if self.root is None:
            return
        self.postorder_traversal(node.left)
        self.postorder_traversal(node.right)
        print(node.data)
    
    
    def insert_level_order(self, data):
        """
        Inserts a new node into the tree using level-order (breadth-first) traversal.

        Args:
            data: The data to be inserted.
        """
        if self.root is None:
            self.root = Node(data)
            return

        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.left is None:
                current.left = Node(data)
                return
            else:
                queue.append(current.left)

            if current.right is None:
                current.right = Node(data)
                return
            else:
                queue.append(current.right)

def maximum_depth(root: Node) -> int: 
    """
        input: Node 
        output: int 
        return maximum depth of binary tree 
    """
    if root is None: 
        return 0 
    return maximum_depth(root.left) + maximum_depth(root.right) + 1

if __name__ == "__main__":
    # Create a binary tree
    tree = BinaryTree(Node(1, 2, 3))
    tree.insert_level_order(1)
    tree.insert_level_order(2)
    tree.insert_level_order(3)
    tree.insert_level_order(4)
    tree.insert_level_order(5)
    tree.insert_level_order(6)
    tree.insert_level_order(7)
    tree.insert_level_order(8)
    print(tree.inorder_traversal(tree.root))
    print(maximum_depth(tree.root))
    