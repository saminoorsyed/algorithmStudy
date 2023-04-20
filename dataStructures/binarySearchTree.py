# Due Date: 5/16/2022
# Description: Implementation of a BST class with the following methods: add(), remove(),
# contains(), inorder_traversal(), find_min(), find_max(), is_empty(), make_empty()

import random
from queue_and_stack import Queue, Stack


class BSTNode:
    """
    Binary Search Tree Node class
    """

    def __init__(self, value: object) -> None:
        """
        Initialize a new BST node
        """
        self.value = value   # to store node's data
        self.left = None     # pointer to root of left subtree
        self.right = None    # pointer to root of right subtree

    def __str__(self) -> str:
        """
        Override string method
        """
        return 'BST Node: {}'.format(self.value)


class BST:
    """
    Binary Search Tree class
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize new Binary Search Tree
        """
        self._root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using pre-order traversal
        """
        values = []
        self._str_helper(self._root, values)
        return "BST pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, node: BSTNode, values: list) -> None:
        """
        Helper method for __str__. Does pre-order tree traversal
        """
        if not node:
            return
        values.append(str(node.value))
        self._str_helper(node.left, values)
        self._str_helper(node.right, values)

    def get_root(self) -> BSTNode:
        """
        Return root of tree, or None if empty
        """
        return self._root

    def is_valid_bst(self) -> bool:
        """
        Perform pre-order traversal of the tree.
        Return False if nodes don't adhere to the bst ordering property.
        This is intended to be a troubleshooting 'helper' method to help
        find any inconsistencies in the tree after the add() or remove()
        operations. Review the code to understand what this method is
        checking and how it determines whether the BST tree is correct.
        """
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                if node.left and node.left.value >= node.value:
                    return False
                if node.right and node.right.value < node.value:
                    return False
                stack.push(node.right)
                stack.push(node.left)
        return True

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        This method adds a new value to the tree. Duplicate values are allowed. If a node with that value is already in the tree, the new value should be added to the right subtree of that node. It must be implemented with O(N) runtime complexity.
        """
        #iterative implementation
        if self.is_empty():
            self._root = BSTNode(value)
        else:
            # finds the appropriate leaf at which to append the new value in O(n) time
            parent = self._root
            current_node = self._root
            while current_node != None:
                parent = current_node
                if value < current_node.value:
                    current_node = current_node.left
                else:
                    current_node = current_node.right

            if value < parent.value:
                parent.left = BSTNode(value)
            else:
                parent.right = BSTNode(value)

    def remove(self, value: object) -> bool:
        """
        This method removes a value from the tree. The method returns True if the value is removed; otherwise, it returns False. It must be implemented with O(N) runtime complexity. NOTE: See ‘Specific Instructions’ for an explanation of which node replaces the deleted node.

        Param: value: object
        """
        # cannot remove a value from an empty tree
        if self.is_empty():
            return False
        if self.contains(value) != True:
            return False

        #if the targeted node is the root node
        if self._root.value == value:
            # the case in which there are two subtrees
            if self._root.left != None and self._root.right != None:
                self._remove_two_subtrees(self._root, self._root)
            # the case in which there are no subtrees
            elif self._root.left == None and self._root.right == None:
                self._remove_no_subtrees(self._root, self._root)
            # the case in which there is at least one subtree
            elif self._root.left != None or self._root.right != None:
                self._remove_one_subtree(self._root, self._root)

        # if the targeted node is not the root node
        else:
            target_parent = self._find_node(value)
            #the right child of the parent node is the target node
            if target_parent.right != None and target_parent.right.value == value:
                target = target_parent.right
                # the case in which the target node has two children
                if target.right != None and target.left != None:
                    self._remove_two_subtrees(target_parent, target)
                # the case in which the target node has one child
                if target.right != None or target.left != None:
                    self._remove_one_subtree(target_parent, target)
                # the case in which the target node has no children
                if target.right == None and target.left == None:
                    self._remove_no_subtrees(target_parent, target)
            elif target_parent.left.value == value:
                target = target_parent.left
                # the case in which the target node has two children
                if target.right != None and target.left != None:
                    self._remove_two_subtrees(target_parent, target)
                # the case in which the target node has one child
                if target.right != None or target.left != None:
                    self._remove_one_subtree(target_parent, target)
                # the case in which the target node has no children
                if target.right == None and target.left == None:
                    self._remove_no_subtrees(target_parent, target)
        return True

    def _remove_no_subtrees(self, parent: BSTNode, node: BSTNode) -> None:
        """
        Removes the node with no children, right or left. 

        Param: parent: BSTNode, node: BSTNode
        return: None
        """
        # removes the target node
        if parent.right == node:
            parent.right = None
        if parent.left == node:
            parent.left = None
        if parent == node:
            self._root = None    

    def _remove_one_subtree(self, parent: BSTNode, node: BSTNode) -> None:
        """
        removes a node that has only one subtree by changing the referencing th on the node's parent
        """
       
        # if the target node is the root node 
        if parent == node:
            if parent.left != None:
                self._root = parent.left
            else:
                self._root = parent.right
        # if the target node is the right child of it's parent 
        if parent.right == node:
            if node.right == None:
                parent.right = node.left
            else:
                parent.right = node.right
        # if the target node is the left child of it's parent
        if parent.left == node:
            if node.right == None:
                parent.left = node.left
            else:
                parent.left = node.right

    def _remove_two_subtrees(self, parent: BSTNode, node: BSTNode) -> None:
        """
        removes a node that has two subtrees by replacing the target node with its inorder succesor rereferencing the target node's left branch as the in order successor's left branch. the parent now points to the inorder successor rather than the target node
        """
        # the case in which the node.right is the in_order successor
        inorder_successor = self._inorder_successor(node)
        if inorder_successor.left == None:
            # the target node is the node to the right of its parent
            if parent.right == node:
                inorder_successor.left = node.left
                parent.right = inorder_successor
            # the target node is the node to the left of its parent
            if parent.left == node:
                inorder_successor.left = node.left
                parent.left = inorder_successor
            # the target node is the root node
            if parent == node:
                self._root = inorder_successor
                inorder_successor.left = parent.left

        else:
            # the case where the inorder successor is not the right child of the target node
            inorder_parent = inorder_successor
            inorder_successor = inorder_successor.left

            # right and left of parent node reassignments that happen in all subcases
            inorder_parent.left = inorder_successor.right
            inorder_successor.right = node.right
            inorder_successor.left = node.left
            
            # the target node is the node to the right of its parent
            if parent.right == node:
                parent.right = inorder_successor
            # the target node is the node to the left of its parent
            if parent.left == node:
                parent.left = inorder_successor
            # the target node is the root node
            if parent == node:
                self._root = inorder_successor
   
    def _inorder_successor(self, node: BSTNode)-> BSTNode:
        """
        iteratively traverses the tree and finds the inorder successor of the input node. If the in order successor is the root of the target node's right subtree, the method return that node. If the in order successor is a different node, the method return the inorder successor's parent node

        Param: node: BSTNode
        return: BSTNode
        """
        # set all nodes to the root of the right subtree
        current_node = node.right
        inorder_successor = current_node
        parent_node = current_node
        # if their is a left child of the right subtree's root loop to find the inorder successor and its parent
        while current_node != None:
            parent_node = inorder_successor
            inorder_successor = current_node
            current_node = current_node.left
        
        return parent_node

    def contains(self, value: object) -> bool:
        """
        This method returns True if the value is in the tree; otherwise, it returns False. If the tree is empty, the method should return False. It must be implemented with O(N) runtime complexity.
        
        Param: value: object
        return: Boolean
        """
        # An empty tree contains no value... I feel like I read that in a fortune cookie at some point
        if self.is_empty():
            return False
        
        check_node = self._find_node(value)
        # the case in which the value is stored in a leaf or the root
        if check_node.value == value:
            return True
        # the cases in which the value is stored on the interior of the tree
        if (check_node.left != None and check_node.left.value == value) or (check_node.right != None and check_node.right.value == value):
            return True
        # the case in which the value is not stored in the tree
        else:
            return False

    def inorder_traversal(self) -> Queue:
        """
        This method will perform an inorder traversal of the tree iteratively, and return a Queue object that contains the values of the visited nodes, in ascending order. If the tree is empty, the method returns an empty Queue. It must be implemented with O(N) runtime complexity.
        
        Param:None
        return: Queue
        """
        
        stack = Stack()
        queue = Queue()
        
        if self.is_empty():
            return queue

        current_node = self._root
        #establish an entry variable when the stack is empty
        while current_node != None or not stack.is_empty():
            if current_node != None:
                stack.push(current_node)
                current_node = current_node.left
            elif not stack.is_empty():
                current_node = stack.pop()
                queue.enqueue(current_node.value)
                current_node = current_node.right
        return queue



    def find_min(self) -> object:
        """
        This method returns the lowest value in the tree. If the tree is empty, the method should return None. It must be implemented with O(N) runtime complexity.
        
        Param: None
        return: object
        """
        if self.is_empty():
            return
        current_node = self._root
        min_node = self._root
        #iterate through the left side of the tree to find the minimum value
        while current_node != None:
            min_node = current_node
            current_node = current_node.left
        return min_node.value
        
    def find_max(self) -> object:
        """
        This method returns the highest value in the tree. If the tree is empty, the method should return None. It must be implemented with O(N) runtime complexity.

        Param: None
        return: object
        """
        if self.is_empty():
            return
        current_node = self._root
        max_node = self._root
        # iterate through the right side of the tree to find the maximum value
        while current_node != None:
            max_node = current_node
            current_node = current_node.right
        
        return max_node.value

    def is_empty(self) -> bool:
        """
        This method returns True if the tree is empty; otherwise, it returns False. It must be implemented with O(1) runtime complexity.
        
        Param: None
        return: Boolean
        """
        return self._root == None

    def make_empty(self) -> None:
        """
        This method removes all of the nodes from the tree. It must be implemented with O(1) runtime complexity.

        Param: None
        return: None
        """
        self._root = None

    def _find_node(self, target_value: object = None, start_node: BSTNode = None) -> BSTNode:
        """
        Iterates through tree starting at the root. If a target value is stored in the tree, this method returns the parent of the node with that value stored as its key; if the root node has the target value stored as its key, this method returns the root node. If the target value is not stored in the tree, this method returns the node at which that target value should be appended.

        Param: start_node:BSTNode, value, target_value: int
        return: BSTNode
        """
        # set all nodes = to the root node so that if the target value is reached early, the root node is returned
        if start_node == None:
            start_node = self._root
        current_node = start_node
        target_node = start_node
        parent_node = start_node
        while current_node != None and current_node.value != target_value:
            parent_node = target_node
            target_node = current_node
            if target_value < target_node.value:
                current_node = target_node.left
            else:
                current_node = target_node.right
        
        # this is the parent node of the target node or the root node if the target value is the root node
        if target_node.value == target_value:
            return parent_node
        # this node is a leaf of the tree at which the target value should be appended
        else:
            return target_node



# ------------------- BASIC TESTING -----------------------------------------

if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),
        (3, 2, 1),
        (1, 3, 2),
        (3, 1, 2),
    )
    for case in test_cases:
        tree = BST(case)
        print(tree)

    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),
        (10, 20, 30, 50, 40),
        (30, 20, 10, 5, 1),
        (30, 20, 10, 1, 5),
        (5, 4, 6, 3, 7, 2, 8),
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        tree = BST(case)
        print('INPUT  :', case)
        print('RESULT :', tree)

    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = BST()
        for value in case:
            tree.add(value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH ADD OPERATION")
    print('add() stress test finished')

    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),
        ((1, 2, 3), 2),
        ((1, 2, 3), 3),
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    tree = BST(case)
    for del_value in case:
        print('INPUT  :', tree, del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    tree = BST(case)
    for _ in case[:-2]:
        root_value = tree.get_root().value
        print('INPUT  :', tree, root_value)
        tree.remove(root_value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH REMOVE OPERATION")
        print('RESULT :', tree)

    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = BST()
    print(tree.contains(0))

    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())

    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
