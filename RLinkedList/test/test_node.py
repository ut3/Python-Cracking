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

import pytest
from RLinkedList import Node, delete_node, insert_node, insert_data
def test_node_create():
    node = Node("parent")
    assert(node != None)

def test_right_type_equal():
    node = Node("parent")
    right = Node("right")
    node.right = right
    assert(node.right is right)

def test_right_type_not_equal():
    node = Node()
    with pytest.raises(ValueError):
        badright = "string"
        node.right = badright
    assert(node.right is None)

def test_node_left():
    node = Node("parent")
    left = Node("left")
    node.left = left
    assert(node.left is left)

def test_left_type_not_equal():
    node = Node()
    with pytest.raises(ValueError):
        badleft = "string"
        node.left = badleft
    assert(node.left is None)

def verify_link(left, right):
    assert(left.right is right)
    assert(right.left is left)

def test_verify_link_negative_left():
    left = Node("left")
    right = Node("right")
    right.left = left
    with pytest.raises(AssertionError):
        verify_link(left, right)

def test_verify_link_negative_right():
    left = Node("left")
    right = Node("right")
    left.right = right
    with pytest.raises(AssertionError):
        verify_link(left, right)

def verify_links(pairs):
    for pair in pairs:
        verify_link(pair[0], pair[1])

def setup_nodes():
    left = Node("left")
    right = Node("right")
    left.left = right
    left.right = right
    right.left = left
    right.right = left
    midleft = insert_data(left, right, "midleft")
    midright = insert_data(midleft, right, "midright")
    verify_links([(right, left), (left, midleft), (midleft, midright), (midright, right)])
    return (left, midleft, midright, right)

def test_delete_left_node():
    (left, midleft, midright, right) = setup_nodes()
    delete_node(left)
    verify_links([(midleft, midright), (midright, right), (right, midleft)])

def test_delete_midleft_node():
    (left, midleft, midright, right) = setup_nodes()
    delete_node(midleft)
    verify_links([(left, midright), (midright, right), (right, left)])

def test_delete_midright_node():
    (left, midleft, midright, right) = setup_nodes()
    delete_node(midright)
    verify_links([(left, midleft), (midleft, right), (right, left)])

def test_delete_right_node():
    (left, midleft, midright, right) = setup_nodes()
    delete_node(right)
    verify_links([(left, midleft), (midleft, midright), (midright, left)])

def test_insert_node_right_left():
    (left, midleft, midright, right) = setup_nodes()
    new = Node("new")
    insert_node(right, left, new)
    verify_links([(left, midleft), (midleft, midright), (midright, right), (right, new), (new, left)])

def test_insert_node_left_midleft():
    (left, midleft, midright, right) = setup_nodes()
    new = Node("new")
    insert_node(left, midleft, new)
    verify_links([(left, new), (new, midleft), (midleft, midright), (midright, right), (right, left)])

def test_insert_node_midleft_midright():
    (left, midleft, midright, right) = setup_nodes()
    new = Node("new")
    insert_node(midleft, midright, new)
    verify_links([(left, midleft), (midleft, new), (new, midright), (midright, right), (right, left)])

def test_insert_node_midright_right():
    (left, midleft, midright, right) = setup_nodes()
    new = Node("new")
    insert_node(midright, right, new)
    verify_links([(left, midleft), (midleft, midright), (midright, new), (new, right), (right, left)])
