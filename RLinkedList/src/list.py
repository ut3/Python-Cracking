# Copyright (c) 2018, J. Rick Ramstetter
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from RLinkedList import Node, delete_node, insert_node, insert_data, Iter
import RUtil
import functools

class List:      
    maxsize = 10000
    head = None # leftmost
    tail = None # rightmost

    def __init__(self):
        return

    def sanity(self):
        # If self.head is None, then self.tail must also be none
        assert(self.head is not None or self.head is None and self.tail is None)
        # If self.tail is not None, then self.head must also be not None
        assert(self.tail is None or self.tail is not None and self.head is not None)
        # If self.head is not None, then self.tail.right should be self.head
        assert(self.head is None or self.head is self.tail.right)
        assert(self.head is None or self.head.left is self.tail)

    def __iter__(self):
        return Iter(self.head, self.tail)

    def is_empty(self):
        self.sanity()
        return self.head is None

    def back(self):
        self.sanity()
        return None if self.tail is None else self.tail.data

    def front(self):
        self.sanity()
        return None if self.head is None else self.head.data

    def size(self):
        self.sanity()
        count = 0
        for _ in self:
            count += 1
        return count

    def insert(self, left, right, value):
        self.sanity()
        if (self.head is None):
            self.head = Node(value)
            self.head.right = self.head
            self.head.left = self.head
            self.tail = self.head             
            return self.head
        return insert_data(left, right, value)

    def push_back(self, value):
        self.tail = self.insert(self.tail, self.head, value)
        
    def push_front(self, value):     
        self.head = self.insert(self.tail, self.head, value)

    def erase(self, node):
        self.sanity()
        if (self.head is None):
            return None
        if (node is self.head and node is self.tail):
            self.head = None
            self.tail = None
            return node.data
        right = delete_node(node)
        if (node is self.head):
            self.head = right
        elif (node is self.tail):
            self.tail = right.left
        return node.data

    def erase_back(self):
        return self.erase(self.tail)

    def erase_front(self):
        return self.erase(self.head)

    def node_at(self, index):       
        i = 0
        for item in self:
            if i == index:
                return item
            i += 1
        return None

    def at(self, index):
        return self.node_at(index).data