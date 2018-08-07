from RLinkedList import Node

class List:
    """back, size, insert"""
    head = None # leftmost
    tail = None # rightmost
    def __init__(self):
        return

    def sanity(self):
        assert(self.head is not None or self.head is None and self.tail is None)
        assert(self.tail is None or self.tail is not None and self.head is not None)
        assert(self.head is None or self.head is self.tail.right)

    def is_empty(self):
        self.sanity()
        return self.head is None

    def size(self):
        self.sanity()
        if (self.is_empty()):
            return 0
        cursor = self.head
        count = 1
        while (cursor is not self.tail and count < 10000):
            count+=1
            cursor = cursor.right
        return count

    def push_back(self, value):
        self.sanity()
        if (self.head is None): 
            self.head = Node(value)
            self.head.right = self.head
            self.head.left = self.head
            self.tail = self.head
            return
        self.tail = Node(value, self.tail, self.head)
        self.head.left.right = self.tail
        self.head.left = self.tail
    
    def back(self):
        self.sanity()
        return None if self.tail is None else self.tail.data

    def erase_back(self):
        self.sanity()
        if (self.tail is None):
            return None
        data = self.tail.data
        if (self.tail is self.head):
            self.head = None
            self.tail = None
            return data
        self.tail.left.right = self.head
        self.head.left = self.tail.left
        self.tail = self.tail.left
        return data

    def front(self):
        self.sanity()
        return None if self.head is None else self.head.data

    def erase_front(self):
        self.sanity()
        if (self.head is None):
            return None
        data = self.head.data
        if (self.tail is self.head):
            self.head = None
            self.tail = None
            return data 
        self.head.right.left = self.tail
        self.tail.right = self.head.right
        self.head = self.head.right
        return data

    def push_front(self, value):     
        self.sanity()
        if (self.head is None): 
            self.head = Node(value)
            self.head.right = self.head
            self.head.left = self.head
            self.tail = self.head
            return
        self.head = Node(value, self.tail, self.head)
        self.tail.right.left = self.head
        self.tail.right = self.head

    def at(self, index):
        self.sanity()
        if (self.is_empty()):
            return None
        cursor = self.head
        i = 0
        while (i < index and cursor is not self.tail):
            print("i:", i, " data:", cursor.data)
            cursor = cursor.right
            i+=1
        return cursor.data