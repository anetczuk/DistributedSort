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
from dsort.master import Master
from dsort import nmerge
from dsort.nmerge import NMerge


class NMergeTest(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_initMasterBuffer(self):
        random.seed(2)
        
        K = 2
        master = Master(K, 2)
        master.randomizeNodes()
        
        merge = NMerge()
        merge.master = master
        
        merge.initMasterBuffer()
        
        self.assertEqual(len(master.nodes), K)
        self.assertEqual(master.nodes[0].data, [3, 2])
        self.assertEqual(master.nodes[1].data, [0, 1])
        
        self.assertEqual(master.buffer, [3, 0])
        self.assertEqual(merge.nodeDataIndex, [0, 0])
        
        
    def test_findBufferMin(self):
        random.seed(2)
        
        K = 3
        master = Master(K, 2)
        master.buffer = [3, 1, 2]
        
        merge = NMerge()
        merge.master = master
        merge.nodeDataIndex = [0, 3, 1]
        
        merge.findBufferMin()
        
        self.assertEqual(merge.bufferMinIndex, 2)
        
        
    def test_sortNaive_nodata(self):
        random.seed(2)
        
        K = 3
        master = Master(K, 0)
        master.randomizeNodes()
        
        merge = NMerge()
        merge.sortNaive(master)
        
        self.assertEqual(len(master.nodes), K)
        self.assertEqual(master.nodes[0].data, [])
        self.assertEqual(master.nodes[1].data, [])
        self.assertEqual(master.nodes[2].data, [])
        
    def test_sortNaive_onenode(self):
        random.seed(2)
        
        K = 1
        master = Master(K, 3)
        master.randomizeNodes()
        
        merge = NMerge()
        merge.sortNaive(master)
        
        self.assertEqual(len(master.nodes), K)
        self.assertEqual(master.nodes[0].data, [0, 1, 2])
        
                
    def test_sortNaive_normal(self):
        random.seed(2)
         
        K = 3
        master = Master(K, 3)
        master.randomizeNodes()
        
#         master.printData()
        
        merge = NMerge()
        merge.sortNaive(master)
         
        self.assertEqual(len(master.nodes), K)
        self.assertEqual(master.nodes[0].buffer, [0, 1, 2])
        self.assertEqual(master.nodes[1].buffer, [3, 4, 5])
        self.assertEqual(master.nodes[2].buffer, [6, 7, 8])


if __name__ == "__main__":
    unittest.main()
    