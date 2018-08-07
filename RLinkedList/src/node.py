
class Node:
    left = None
    right = None
    data = None
    def __init__(self, data = None):
        self.data = data

    def __setattr__(self, name, value):
        if name == "left" or name == "right":
            self.enforce_type(name, value)
        self.__dict__[name] = value

    def enforce_type(self, name, value):
        if (value is not None and not isinstance(value, Node)):
            raise ValueError("set_link: node type did not match parent: newnode=", name, " valuetype=", type(value), " value=", value)

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