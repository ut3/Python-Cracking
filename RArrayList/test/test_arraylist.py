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
from RArrayList import ArrayList, pack_frame, unpack_frame
import numpy as np
import pickle as pk

def test_create_arraylist():
    list = ArrayList()
    assert(None is not list)
    assert(list.is_empty())

def test_pack_unpack():
    input = "input string"
    pkinput = pk.dumps(input, pk.HIGHEST_PROTOCOL)
    serialized = pack_frame(input)
    assert(0 == serialized[0])
    assert(len(pkinput) == serialized[1])
    assert(pkinput == serialized[2:len(serialized)].tobytes('C'))
    assert(input == unpack_frame(serialized))

def test_pack_too_big():
    input = "1" * 256
    with pytest.raises(ValueError):
        pack_frame(input)

def test_unpack_negative_path():
    with pytest.raises(ValueError):
        unpack_frame("this is not a numpy array")
    with pytest.raises(ValueError):
        unpack_frame(None)
    with pytest.raises(ValueError):
        unpack_frame(0)
    with pytest.raises(ValueError):
        unpack_frame(1)

def test_push_back_one():
    list = ArrayList()
    data = "a thing"
    list.push_back(data)
    assert(0 != len(list.storage))
    assert(ArrayList.initialSize == len(list.storage))
    assert(1 == list.size())
    assert(len(pack_frame(data)) == list.bytesConsumed)
    assert(data == list.at(0))

def test_push_back_two():
    list = ArrayList()
    data1 = "first"
    list.push_back(data1)
    explen = len(pack_frame(data1))
    data2 = "second"
    list.push_back(data2)
    explen += len(pack_frame(data2))
    assert(2 == list.size())
    assert(explen == list.bytesConsumed)
    assert(data1 == list.at(0))
    assert(data2 == list.at(1))

def test_push_back_three():
    list = ArrayList()
    data1 = "first"
    list.push_back(data1)
    explen = len(pack_frame(data1))
    data2 = "second"
    list.push_back(data2)
    explen += len(pack_frame(data2))
    data3 = "third"
    list.push_back(data3)
    explen += len(pack_frame(data3))
    assert(3 == list.size())
    assert(explen == list.bytesConsumed)
    for i in range(explen, len(list.storage)):
        assert(0 == list.storage[i])
    assert(data1 == list.at(0))
    assert(data2 == list.at(1))
    assert(data3 == list.at(2))

def test_push_back_grow():
    list = ArrayList()
    data = "a" * 150
    list.push_back(data)
    explen = len(pack_frame(data))
    assert(1 == list.size())
    assert(explen == list.bytesConsumed)
    assert(256 == len(list.storage))
    for i in range(explen, len(list.storage)):
        assert(0 == list.storage[i])
    assert(0 != list.storage[explen - 1])
    assert(1 == list.timesGrown)

def test_push_back_grow_three():
    list = ArrayList()
    data = "a" * 200
    list.push_back(data) # grows to 128 * 2 = 256
    explen = len(pack_frame(data))
    assert(explen == list.bytesConsumed)
    assert(list.initialSize * list.growthFactor**1 == len(list.storage))
    assert(1 == list.timesGrown)

    data = "b" * 200
    list.push_back(data) # grows to 256 * 2 = 512
    explen += len(pack_frame(data))
    assert(explen == list.bytesConsumed)
    assert(list.initialSize * list.growthFactor**2 == len(list.storage))
    assert(2 == list.timesGrown)

    data = "c" * 200
    list.push_back(data) # grows to 512 * 2 = 1024
    explen += len(pack_frame(data))
    assert(explen == list.bytesConsumed)
    assert(list.initialSize * list.growthFactor**3 == len(list.storage))
    assert(3 == list.timesGrown)

    assert(3 == list.size())
    for i in range(explen, len(list.storage)):
        assert(0 == list.storage[i])
    assert(0 != list.storage[explen - 1])
    assert(3 == list.elementCount)


def test_erase():
    list = ArrayList()
    for i in range(0,10):
        list.push_back("s" + str(i))
        assert(i + 1 == list.size())
    assert(10 == list.size())
    for i in range(10, 0, -1):
        elem = list.erase_last()
        assert("s" + str(i-1) == elem)
        assert(i - 1 == list.size())
    assert(0 == list.size())
