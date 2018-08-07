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

def tes_set_0():
    return

def test_set_100():
    return