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
#
# This code is educational. It is not meant to be performant.

import sys, numpy as np, pickle as pk
from sortedcontainers import SortedDict


# Data format is: 0, object length 0-256, data
# Input is an object
# Output is a numpy array
def pack(value):
    pickled = pk.dumps(value, pk.HIGHEST_PROTOCOL)
    if (len(pickled) is 0):
        raise ValueError("pickled representation of", value, "has size 0")
    if (len(pickled) > 255):
        raise ValueError("pickled representation is bigger than 255,", len(pickled))
    out = np.zeros(len(pickled) + 2, np.uint8, 'C')
    out[0] = 0
    out[1] = len(pickled)
    for i in range(0, len(pickled)):
        out[2+i] = pickled[i]
    return out


# Data format is: 0 byte, one byte object length 0-256, N bytes data
# Output is an object
def unpack(value):
    if not isinstance(value, np.ndarray):
        raise ValueError("Expecting a np.ndarray as input")
    byteval = value[2:(2 + value[1])].tobytes('C')
    return pk.loads(byteval)



class ArrayList:
    initialSize = 128 # bytes
    growthFactor = 2

    def __init__(self):
        # Numpy 1d c-style array of uint8
        self.storage = None

        # Number of nonzero bytes in that array
        # "0" is a sentinal value for this data structure
        # This will be the index of the first unset (still 0) array byte.
        self.bytesConsumed = 0

        # Number of elements in the array. Elements may be more than one byte.
        self.elementCount = 0

        # Map index to byte offset
        self.dictionary = SortedDict()


    def bytes_per_element(self):
        if self.elementCount is 0:
            avg = 0
        else:
            avg = self.bytesConsumed / self.elementCount
        assert(0 != avg)
        return avg


    def is_empty(self):
        return self.elementCount == 0


    def push_back(self, value):
        if value is None:
            raise ValueError("attempt to insert None")
        if value is 0:
            raise ValueError("can't insert 0 into ArrayList")

        # Allocate initial storage
        if self.storage is None:
            self.storage = np.zeros(self.initialSize, np.uint8, 'C')

        packed = pack(value)

        # Grow
        if self.bytesConsumed + len(packed) > self.storage.size:
            old = self.storage
            self.storage = np.zeros(len(old) * self.growthFactor, np.uint8, 'C')
            i = 0
            for _ in np.nditer(old, order='C'):
                self.storage[i] = old[i]

        # Assign
        for i in range(0, len(packed)):
            self.storage[self.bytesConsumed + i] = packed[i]
            #print("storage[", self.bytesConsumed + i, "] = ", packed[i])
        self.dictionary[self.elementCount] = self.bytesConsumed
        self.bytesConsumed = self.bytesConsumed + i + 1
        self.elementCount += 1


    def erase_last(self):
        if (0 is self.elementCount):
            return
        start = self.dictionary[self.elementCount - 1]
        length = self.storage[start + 1]
        # data = self.storage[start : start + length + 2]
        for i in range(start, start + length + 2):
            self.storage[i] = 0
        self.elementCount -= 1
        assert(0 <= self.elementCount)
        self.bytesConsumed -= length - 2
        assert(0 <= self.bytesConsumed)
        # for i in range(0, len(self.storage)):
        #     print("storage[", i, "] = ", self.storage[i])


    def size(self):
        return self.elementCount


    def at(self, index):
        start = self.dictionary[index]
        length = self.storage[start + 1]
        data = self.storage[start : start + length + 2]
        return unpack(data)