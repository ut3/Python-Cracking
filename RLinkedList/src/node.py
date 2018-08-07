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

class Iter:
    tail = None
    cursor = None
    count = 0
    end = False
    maxsize = 10000

    def __init__(self, cursor, tail):
        self.cursor = cursor
        self.tail = tail

    def __iter__(self):
        return self

    def __next__(self):
        assert(self.count < self.maxsize)
        self.count += 1
        
        # Iter already done, or iter for empty list
        if self.end or None is self.cursor:
            self.end = True
            raise StopIteration

        # Last Node
        if self.cursor is self.tail:
            self.end = True               
            return self.cursor

        old = self.cursor
        self.cursor = self.cursor.right
        return old
    