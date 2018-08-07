import pytest
import RLinkedList

def test_list_create():
    list = RLinkedList.List()
    assert(list != None)

def test_size_0():
    list = RLinkedList.List()
    assert(0 == list.size())
    assert(list.is_empty())
    assert(None == list.front())

def test_size_1():
    list = RLinkedList.List()
    list.push_back("s1")
    assert(1 == list.size())
    assert("s1" == list.back())
    assert(not list.is_empty())
    assert("s1" == list.front())

def test_size_2():
    list = RLinkedList.List()
    list.push_back("s1")
    list.push_back("s2")
    assert(2 == list.size())
    assert("s2" == list.back())
    assert("s1" == list.front())

def test_size_3():
    list = RLinkedList.List()
    list.push_back("s1")
    list.push_back("s2")
    list.push_back("s3")
    assert(3 == list.size())
    assert("s3" == list.back())
    assert("s1" == list.front())

def test_size_1000():
    list = RLinkedList.List()
    for i in range(0, 1000, 1):
        list.push_back("s" + str(i))
        assert("s" + str(i) == list.back())
        assert("s0" == list.front())
    assert(1000 == list.size())

def test_erase_back_1():
    list = RLinkedList.List()
    list.push_back("s1")
    newNode = list.back()
    newNodeErased = list.erase_back()
    assert(newNode == newNodeErased)
    assert(list.is_empty())
    assert(None == list.front())

def test_erase_back_3():
    list = RLinkedList.List()
    list.push_back("s1")
    list.push_back("s2")
    list.push_back("s3")
    back = list.erase_back()
    assert("s3" == back)
    back = list.erase_back()
    assert("s2" == back)
    back = list.erase_back()
    assert("s1" == back)
    assert(list.is_empty())

def test_erase_back_1000():
    list = RLinkedList.List()
    for i in range(1, 1001, 1):
        list.push_back("s" + str(i))
    for i in range(1000, 1, -1):
        value = list.erase_back()
        assert("s" + str(i) == value)
        assert("s" + str(i-1) == list.back())
        assert("s1" == list.front())
    # s1 remains
    value = list.erase_back()
    assert("s1" == value)
    assert(None == list.front())
    assert(None == list.back())

def test_erase_front_1():
    list = RLinkedList.List()
    list.push_back("s1")
    newNode = list.back()
    newNodeErased = list.erase_front()
    assert(newNode == newNodeErased)
    assert(list.is_empty())
    assert(None == list.front())

def test_erase_front_3():
    list = RLinkedList.List()
    list.push_back("s1")
    list.push_back("s2")
    list.push_back("s3")
    front = list.erase_front()
    assert("s1" == front)
    front = list.erase_front()
    assert("s2" == front)
    front = list.erase_front()
    assert("s3" == front)
    assert(list.is_empty())

def test_erase_front_1000():
    list = RLinkedList.List()
    for i in range(1, 1001, 1):
        list.push_back("s" + str(i))
    for i in range(1, 1000, 1):
        value = list.erase_front()
        assert("s" + str(i) == value)
        assert("s" + str(i+1) == list.front())
    # s1000 remains
    value = list.erase_front()
    assert("s1000" == value)
    assert(None == list.front())
    assert(None == list.back())
    

def test_front_size_1():
    list = RLinkedList.List()
    list.push_front("s1")
    assert(1 == list.size())
    assert("s1" == list.front())
    assert("s1" == list.at(0))
    assert(not list.is_empty())
    assert("s1" == list.back())

def test_front_size_2():
    list = RLinkedList.List()
    list.push_front("s1")
    list.push_front("s2")
    assert(2 == list.size())
    assert("s1" == list.back())
    assert("s1" == list.at(1))
    assert("s2" == list.at(0))
    assert("s2" == list.front())

def test_front_size_3():
    list = RLinkedList.List()
    list.push_front("s1")
    list.push_front("s2")
    list.push_front("s3")
    assert(3 == list.size())
    assert("s1" == list.back())
    assert("s3" == list.front())
    assert("s3" == list.at(0))
    assert("s2" == list.at(1))
    assert("s1" == list.at(2))

def test_front_size_1000():
    list = RLinkedList.List()
    for i in range(1, 1001, 1):
        list.push_front("s" + str(i))
        assert("s1" == list.back())
        assert("s" + str(i) == list.front())    
    assert(1000 == list.size())

def test_at_size_100():
    list = RLinkedList.List()
    for i in range(0, 101, 1):
        list.push_back("s" + str(i))
    for i in range(0, 101, 1):
        assert("s" + str(i) == list.at(i))

def test_at_front_size_100():
    list = RLinkedList.List()
    for i in range(0, 101, 1):
        list.push_front("s" + str(i))
    for i in range(100, 0, 1):
        assert("s" + str(i) == list.at(i))