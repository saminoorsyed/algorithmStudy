# Due Date: 5/16/22
# Description: implementation of an AVL tree with the following overridden methods: add(), remove()


# import random
# from queue_and_stack import Queue, Stack
# from bst import BSTNode, BST


class AVLNode(BSTNode):
    """
    AVL Tree Node class. Inherits from BSTNode
    """
    def __init__(self, value: object) -> None:
        """
        Initialize a new AVL node
        """
        # call __init__() from parent class
        super().__init__(value)

        # new variables needed for AVL
        self.parent = None
        self.height = 0

    def __str__(self) -> str:
        """
        Override string method
        """
        return 'AVL Node: {}'.format(self.value)


class AVL(BST):
    """
    AVL Tree class. Inherits from BST
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize a new AVL Tree
        """
        # call __init__() from parent class
        super().__init__(start_tree)

    def __str__(self) -> str:
        """
        Return content of AVL in human-readable form
        """
        values = []
        super()._str_helper(self._root, values)
        return "AVL pre-order { " + ", ".join(values) + " }"

    def is_valid_avl(self) -> bool:
        """
        Perform pre-order traversal of the tree. Return False if there
        are any problems with attributes of any of the nodes in the tree.

        This is intended to be a troubleshooting 'helper' method to help
        find any inconsistencies in the tree after the add() or remove()
        operations. Review the code to understand what this method is
        checking and how it determines whether the AVL tree is correct.

        """
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                # check for correct height (relative to children)
                left = node.left.height if node.left else -1
                right = node.right.height if node.right else -1
                if node.height != 1 + max(left, right):
                    return False

                if node.parent:
                    # parent and child pointers are in sync
                    if node.value < node.parent.value:
                        check_node = node.parent.left
                    else:
                        check_node = node.parent.right
                    if check_node != node:
                        return False
                else:
                    # NULL parent is only allowed on the root of the tree
                    if node != self._root:
                        return False
                stack.push(node.right)
                stack.push(node.left)
        return True

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        TODO: Write your implementation
        """
        # insert key, value into tree like normal BST insertion
        #iterative implementation
        if self.is_empty():
            self._root = AVLNode(value)
            return
        else:
            # finds the appropriate leaf at which to append the new value in O(n) time
            parent = self._root
            current_node = self._root
            while current_node != None:
                parent = current_node
                if value < current_node.value:
                    current_node = current_node.left
                elif value > current_node.value:
                    current_node = current_node.right
                else:
                    return

        # n ← newly inserted node
        new_node = AVLNode(value)
        new_node.parent = parent
        if value < parent.value:
            parent.left = new_node
        elif value > parent.value:
            parent.right = new_node
        # while p is not NULL:
        while parent:
            #rebalance(p)
            self._rebalance(parent)
            #p ← p.parent
            parent = parent.parent
        

    def remove(self, value: object) -> bool:
        """
        TODO: Write your implementation
        """
        # remove key from tree like normal BST removal
        # cannot remove a value from an empty tree
        if self.is_empty() or not self.contains(value):
            return False
        # find the correct node and store it's value
        node = self._find_node(value)
        if value > node.value:
            node = node.right
        if value < node.value:
            node = node.left
        print(node.value)
        # remove if there is no subtree
        if not node.right and not node.left:
            if node == self._root:
                self._remove_no_subtrees(node,node)
            else:
                self._remove_no_subtrees(node.parent, node)
        # remove if there are two subtrees
        if node.right and node.left:
            if node == self._root:
                self._remove_two_subtrees(node, node)
            else:
                self._remove_two_subtrees(node.parent, node)
        # remove if there is only one subtree
        if node.right or node.left:
            if node == self._root:
                self._remove_one_subtree(node, node)
            else:
                self._remove_one_subtree(node.parent, node)
        return True
        
        # p ← lowest modified node (e.g. parent of removed node)
        removed_parent = node.parent
        # while p is not NULL:
        while removed_parent:
        #     rebalance(p)
            rebalance(removed_parent)
        #     p ← p.parent
            removed_parent = removed_parent.parent
        

    # Experiment and see if you can use the optional                         #
    # subtree removal methods defined in the BST here in the AVL.            #
    # Call normally using self -> self._remove_no_subtrees(parent, node)     #
    # You need to override the _remove_two_subtrees method in any case.      #
    # Remove these comments.                                                 #
    # Remove these method stubs if you decide not to use them.               #

    def _remove_two_subtrees(self, parent: AVLNode, node: AVLNode) -> None:
        """
        TODO: Write your implementation
        """
        pass

    # It's highly recommended to implement                          #
    # the following methods for balancing the AVL Tree.             #
    # Remove these comments.                                        #
    # Remove these method stubs if you decide not to use them.      #
    # Change these methods in any way you'd like.                   #

    def _balance_factor(self, node: AVLNode) -> int:
        """
        TODO: Write your implementation
        """
        right_height = node.right.height +1 if node.right is not None else 0
        left_height = node.left.height +1 if node.left is not None else 0
        balance_factor = right_height - left_height
        return balance_factor

    def _get_height(self, node: AVLNode) -> int:
        """
        TODO: Write your implementation
        """
        return node.height if node else -1


    def _rotate_left(self, node: AVLNode) -> AVLNode:
        """
        TODO: Write your implementation
        """
        # c ← n.right
        new_parent = node.right
        # n.right ← c.left
        node.right = new_parent.left
        # if n.right is not NULL:
        if node.right is not None:
            #n.right.parent ← n
            node.right.parent = node
        # c.left ← n
        new_parent.left = node
        # n.parent ← c
        node.parent = new_parent
        # updateHeight(n)
        self._update_height(node)
        # updateHeight(c)
        self._update_height(new_parent)
        # return c
        return new_parent

    def _rotate_right(self, node: AVLNode) -> AVLNode:
        """
        TODO: Write your implementation
        """
        # c ← n.left
        new_parent = node.left
        # n.left ← c.right
        node.left = new_parent.right
        # if n.left is not NULL:
        if node.left is not None:
            #n.left.parent ← n
            node.left.parent = node
        # c.right ← n
        new_parent.right = node
        # n.parent ← c
        node.parent = new_parent
        # updateHeight(n)
        self._update_height(node)
        # updateHeight(c)
        self._update_height(new_parent)
        # return c
        return new_parent

    def _update_height(self, node: AVLNode) -> None:
        """
        TODO: Write your implementation
        """
        #n.height ← MAX(height(n.left), height(n.right)) + 1

        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1
        #print(node.height)

    def _rebalance(self, node: AVLNode) -> None:
        """
        TODO: Write your implementation
        """
        subtree_parent = node.parent
        # if balanceFactor(n) < -1:
        balance = self._balance_factor(node)
        if balance < -1:
            # if balanceFactor(n.left) > 0:
            if self._balance_factor(node.left) > 0:
                #n.left ← rotateLeft(n.left)
                node.left = self._rotate_left(node.left)
                #n.left.parent ← n
                node.left.parent = node
            # newSubtreeRoot ← rotateRight(n)
            new_subtree = self._rotate_right(node)
            # newSubtreeRoot.parent ← n.parent
            new_subtree.parent = subtree_parent
            # n.parent.left or n.parent.right ← newSubtreeRoot
            if subtree_parent is None:
                self._root = new_subtree
                return
            if new_subtree.value < subtree_parent.value:
                subtree_parent.left = new_subtree
            elif new_subtree.value > subtree_parent.value:
                subtree_parent.right = new_subtree
        # else if balanceFactor(n) > 1:
        elif balance > 1:
            #if balanceFactor(n.right) < 0:
            if self._balance_factor(node.right) < 0:
                #n.right ← rotateRight(n.right)
                node.right = self._rotate_right(node.right)
                #n.right.parent ← n
                node.right.parent = node
            # newSubtreeRoot ← rotateLeft(n)
            new_subtree = self._rotate_left(node)
            # newSubtreeRoot.parent ← n.parent
            new_subtree.parent = subtree_parent
            # n.parent.left or n.parent.right ← newSubtreeRoot
            if subtree_parent is None:
                self._root = new_subtree
                return
            elif new_subtree.value < subtree_parent.value:
                subtree_parent.left = new_subtree
            elif new_subtree.value > subtree_parent.value:
                subtree_parent.right = new_subtree
        else:
            #updateHeight(n)
            self._update_height(node)
    

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1,2, 3),  # RR
        (3, 2, 1),  # LL
        (1, 3, 2),  # RL
        (3, 1, 2),  # LR
    )
    for case in test_cases:
        tree = AVL(case)
        print(tree)

    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),   # RR, RR
        (10, 20, 30, 50, 40),   # RR, RL
        (30, 20, 10, 5, 1),     # LL, LL
        (30, 20, 10, 1, 5),     # LL, LR
        (5, 4, 6, 3, 7, 2, 8),  # LL, RR
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        tree = AVL(case)
        print('INPUT  :', case)
        print('RESULT :', tree)
    #tree = AVL([6, 10, 8, 6, 20, 10, 3, 7, 13, -6, 19, -19, -18, -4, 17, 15, -18, -1, -12, -7, -16, 3, 15, -20, 4, -2, 16, 0, 19, 16])
    
    
    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = AVL()
        for value in case:
            tree.add(value)
        if not tree.is_valid_avl():
            raise Exception("PROBLEM WITH ADD OPERATION")
    print('add() stress test finished')

    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),  # no AVL rotation
        ((1, 2, 3), 2),  # no AVL rotation
        ((1, 2, 3), 3),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),  # no AVL rotation
    )
    for case, del_value in test_cases:
        tree = AVL(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),  # RR
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),  # LL
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),  # RL
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),  # LR
    )
    for case, del_value in test_cases:
        tree = AVL(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    tree = AVL(case)
    for del_value in case:
        print('INPUT  :', tree, del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    tree = AVL(case)
    for _ in case[:-2]:
        root_value = tree.get_root().value
        print('INPUT  :', tree, root_value)
        tree.remove(root_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 5")
    print("-------------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = AVL(case)
        for value in case[::2]:
            tree.remove(value)
        if not tree.is_valid_avl():
            raise Exception("PROBLEM WITH REMOVE OPERATION")
    print('remove() stress test finished')

    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = AVL([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = AVL()
    print(tree.contains(0))

    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())

    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = AVL()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = AVL()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)