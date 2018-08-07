from RLinkedList import Node, delete_node, insert_node, insert_data
import functools

class List:
    """back, size, insert"""
    maxsize = 1000000
    head = None # leftmost
    tail = None # rightmost
    def __init__(self):
        return

    def sanity(self):
        assert(self.head is not None or self.head is None and self.tail is None)
        assert(self.tail is None or self.tail is not None and self.head is not None)
        assert(self.head is None or self.head is self.tail.right)
    
    def __create_initial_node(self, value):
        self.head = Node(value)
        self.head.right = self.head
        self.head.left = self.head
        self.tail = self.head 

    def __iter__(self):
        self.sanity()
        cursor = self.head
        count = 1
        while (cursor is not self.tail and count < self.maxsize):
            count+=1
            yield cursor
            cursor = cursor.right
        assert(self.maxsize != count)

    def is_empty(self):
        self.sanity()
        return self.head is None

    def back(self):
        self.sanity()
        return None if self.tail is None else self.tail.data

    def front(self):
        self.sanity()
        return None if self.head is None else self.head.data

    def accumulate_nodes(self, fxn):
        accumulated = None
        for node in self:
            accumulated = fxn(node, accumulated)
        return accumulated

    def size(self):
        add = lambda node, count: 2 if None is count else count + 1
        count = self.accumulate_nodes(add)
        if None is count:
            return 0 if None is self.head else 1
        return count

    def push_back(self, value):
        self.sanity()
        if (self.head is None): 
            self.__create_initial_node(value)
            return
        self.tail = insert_data(self.tail, self.head, value)
        
    def push_front(self, value):     
        self.sanity()
        if (self.head is None): 
            self.__create_initial_node(value)
            return
        self.head = insert_data(self.tail, self.head, value)

    def erase_back(self):
        self.sanity()
        if (self.tail is None):
            return None
        data = self.tail.data
        if (self.tail is self.head):
            self.head = None
            self.tail = None
            return data
        self.tail = delete_node(self.tail).left
        return data

    def erase_front(self):
        self.sanity()
        if (self.head is None):
            return None
        data = self.head.data
        if (self.tail is self.head):
            self.head = None
            self.tail = None
            return data 
        self.head = delete_node(self.head)
        return data

    def node_at(self, index):
        cursor = self.head
        i = 0
        while (i < index and cursor is not self.tail and i < self.maxsize):
            print("i:", i, " data:", cursor.data)
            cursor = cursor.right
            i+=1
        return cursor

    def delete(self, node):
        return delete_node(node)

    def set(self, index, value):
        if isinstance(index, int):
            self.set(self.node_at(index), value)
        elif isinstance(index, Node):
            if value is None:
                self.delete(index)
            else:
                index.data = value
        else:
            raise ValueError("Data type is not Node or int:", type(index))

    def at(self, index):
        return self.node_at(index).data