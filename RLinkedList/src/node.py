
class Node:
    def __init__(self, data = None, left = None, right = None):
        self.set_child("left", left)
        self.set_child("right", right)
        self.data = data

    def __setattr__(self, name, value):
        if name == "left" or name == "right":
            self.set_child(name, value)
        self.__dict__[name] = value

    def set_child(self, name, value):
        """Set a child node iff the new link will be of the same type as self"""
        if (value is not None and not isinstance(value, Node)):
            raise ValueError("set_child: child type did not match parent: child=", name, " valuetype=", type(value), " value=", value)
        self.__dict__[name] = value 

    def __repr__(self):
        return str(self.data)

def delete_node(node):
    right = node.right
    left = node.left
    right.left = left
    left.right = right
    return right

def insert_node(left, right, node):
    node.left = left
    node.right = right
    left.right = node
    right.left = node
    return node

def insert_data(left, right, data): 
    node = Node(data)
    return insert_node(left, right, node)