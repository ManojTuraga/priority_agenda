class BNode:
    def __init__(self, entry):
        """Function initializes a BNode object with an entry, left child, and right child."""
        self.entry = entry
        self.left = None
        self.right = None

    def get_left(self):
        """Function returns the Nodes left child."""
        return self.left

    def get_right(self):
        """Function returns the Nodes right child."""
        return self.right

    def get_entry(self):
        """Function returns the Nodes entry."""
        return self.entry

    def set_left(self, new_entry):
        """Function sets the left child of the Node."""
        self.left = new_entry

    def set_right(self, new_entry):
        """Function sets the right child of the Node."""
        self.right = new_entry

    def set_entry(self, new_entry):
        """Function sets the entry of the Node."""
        self.entry = new_entry

    def has_two_children(self):
        """Function retuns True if a Node has 2 children that are not None."""
        return self.right is not None and self.left is not None

    def auto_get(self, value):
        """Function returns the specific child that contains a certain value."""
        if isinstance(self.left, BNode) and self.left.entry == value:
            return self.left

        elif isinstance(self.right, BNode) and self.right.entry == value:
            return self.right

        else:
            raise RuntimeError("Error! Either left and children are not node types of value is not in the left or right children")
