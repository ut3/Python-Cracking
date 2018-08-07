import pytest
import RLinkedList

def test_node_create():
    node = RLinkedList.Node("parent")
    assert(node != None)

def test_right_type_equal():
    node = RLinkedList.Node("parent")
    right = RLinkedList.Node("right")
    node.right = right
    assert(node.right is right)

def test_right_type_not_equal():
    node = RLinkedList.Node()
    with pytest.raises(ValueError):
        badright = "string"
        node.right = badright
    assert(node.right is None)

def test_node_left():
    node = RLinkedList.Node("parent")
    left = RLinkedList.Node("left")
    node.left = left
    assert(node.left is left)    

def test_left_type_not_equal():
    node = RLinkedList.Node()
    with pytest.raises(ValueError):
        badleft = "string"
        node.left = badleft
    assert(node.left is None)
