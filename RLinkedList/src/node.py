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
        if (value is not None and type(self) != type(value)):
            raise ValueError("set_child: child type did not match parent: child=", name, " valuetype=", type(value), " value=", value)
        self.__dict__[name] = value