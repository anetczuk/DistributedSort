# MIT License
# 
# Copyright (c) 2017 Arkadiusz Netczuk <dev.arnet@gmail.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

import unittest
import random
from dsort.node import Node


class NodeTest(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testRandomizeData(self):
        random.seed(1)
        
        node = Node(3)
        node.randomizeData(5)
        
        self.assertEqual(len(node.data), 3)
        self.assertEqual(node.data[0], 5)
        self.assertEqual(node.data[1], 7)
        self.assertEqual(node.data[2], 6)
        
    def testSortData(self):
        random.seed(1)
        
        node = Node(3)
        node.randomizeData(5)
        node.sortData()
        
        self.assertEqual(len(node.data), 3)
        self.assertEqual(node.data[0], 5)
        self.assertEqual(node.data[1], 6)
        self.assertEqual(node.data[2], 7)
         
#     def testNameB(self):
#         self.assertEqual(0, 1)


if __name__ == "__main__":
    unittest.main()
    