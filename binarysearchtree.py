'''
Author: Manoj Turaga
KUID: 3056848
Date: 04/20/2022
Lab: lab09
Last modified: 05/04/2022
Purpose: Program is an implementation of the Binary Node class, which creates a Binary Node object
'''

from bnode import BNode

class BinarySearchTree:
    def __init__(self):
        """Initalizes a BinarySearchTree object with a root reference."""
        self._root = None

    def add(self, entry):
        """Function is a public facing function that adds an entry to the BST, using a recursive helper function if needed."""
        if self._root == None:
            new_node = BNode(entry)
            self._root = new_node

        else:
            self._rec_add(entry, self._root)

    def _rec_add(self, entry, current_node):
        """Function recursivly adds new entries to the BinarySearchTree object."""
        if entry == current_node.entry:
            raise RuntimeError(f"Error! Cannot add this entry.\n\tThere is already a value with this key:\n\tThis is the existing value with the given key\n\t{current_node.entry}")

        if entry < current_node.entry:
            if current_node.left == None:
                new_node = BNode(entry)
                current_node.left = new_node

            else:
                self._rec_add(entry, current_node.left)

        if entry > current_node.entry:
            if current_node.right == None:
                new_node = BNode(entry)
                current_node.right = new_node

            else:
                self._rec_add(entry, current_node.right)

    def search(self, key):
        """Function is a public facing function that returns True if a value is in the BinarySearchTree object using a recursive helper function."""
        return self._rec_search(key, self._root)
            

    def _rec_search(self, key, current_node):
        """Function recursivley checks if a given value is in the BinarySearchTree Object."""
        if current_node != None:
            if current_node.entry == key:
                return current_node.entry

            if current_node.entry < key:
                return self._rec_search(key, current_node.right)

            if current_node.entry > key:
                return self._rec_search(key, current_node.left)

        raise RuntimeError("Error! Value is not in the Binary Search Tree")

    def traversal(self, function):
        """Function is a public facing function that traverses through the BinarySearchTree by calling a helper function."""
        if self._root is None:
            raise RuntimeError("Cannot traverse an empty BST")

        function(self._root)

    def in_order(self, current_node):
        """Function recursivley traverses the BinarySearchTree in order."""
        if current_node.left is not None:
            self.in_order(current_node.left)

        if current_node.entry is not None:
            print(current_node.entry)

        if current_node.right is not None:
            self.in_order(current_node.right)

    def pre_order(self, current_node, state=True):
        """Function recursivley traverses the BinarySearchTree pre order."""
        f = open("database.txt", 'w')
        f.close()
        output_file = open("database.txt", 'a')
        if current_node.entry is not None:
            output_file.write(str(current_node.entry) + '\n')
            
        if current_node.left is not None:
            self.pre_order(current_node.left)

        if current_node.right is not None:
            self.pre_order(current_node.right)

        output_file.close()

    def post_order(self, current_node):
        """Function recursivley traverses the BinarySearchTree post order."""
        if current_node.left is not None:
            self.post_order(current_node.left)

        if current_node.right is not None:
            self.post_order(current_node.right)

        if current_node.entry is not None:
            print(current_node.entry)

    def remove(self, value):
        """Function is a public facing function that removes a value in a BST by utilizing a recursive helper function."""
        value = self._rec_remove(value, self._root)

        if isinstance(value, BNode) and self._root.entry == value.entry:
            if self._root.left is None:
                self._root = self._root.right

            else:
                self._root = self._root.left

            return value.entry

        return value
        
    def _rec_remove(self, value, current_node):
        """Function is a recursive function that removes a given values from the BST."""
        if current_node is None:
            raise RuntimeError('Error! Value not in BST')

        if current_node.entry == value:
            if current_node.left is not None and current_node.right is not None:
                jumper = current_node.left

                while jumper.right is not None:
                    jumper = jumper.right

                temp = current_node.entry
                current_node.entry = self._rec_remove(jumper.entry, current_node)

                return temp

            else:
                return current_node
            
        if current_node.entry > value:
            node_to_remove = self._rec_remove(value, current_node.left)

            if isinstance(node_to_remove, BNode):
                if node_to_remove.left is None:
                    current_node.left = node_to_remove.right
                    node_to_remove.right = None

                else:
                    current_node.left = node_to_remove.left
                    node_to_remove.left = None

                return node_to_remove.entry

            return node_to_remove
                
        if current_node.entry < value:
            node_to_remove = self._rec_remove(value, current_node.right)

            if isinstance(node_to_remove, BNode):
                if node_to_remove.left is None:
                    current_node.right = node_to_remove.right
                    node_to_remove.right = None

                else:
                    current_node.right = node_to_remove.left
                    node_to_remove.left = None

                return node_to_remove.entry

            return node_to_remove

    def deep_copy(self, other):
        """Function is a public facing function that utliizes a recursive helper function to copy the BST into another BST."""
        self._deep_copy(self._root, other)

    def _deep_copy(self, current_node, other):
        """Function is a recursive function that copies a BST into another BST."""
        if self._root is not None:
            if current_node.entry is not None:
                other.add(current_node.entry)
            
            if current_node.left is not None:
                self._deep_copy(current_node.left, other)

            if current_node.right is not None:
                self._deep_copy(current_node.right, other)
    
