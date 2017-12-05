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


class MasterTest(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testRandomizeNodes(self):
        random.seed(2)
        
        N = 2
        K = 3
        master = Master(N, K)
        master.randomizeNodes()
        
        self.assertEqual(len(master.nodes), N)
        node = master.nodes[1]
        
        self.assertEqual(len(node.data), K)
        self.assertEqual(node.data[0], 3)
        self.assertEqual(node.data[1], 5)
        self.assertEqual(node.data[2], 4)


if __name__ == "__main__":
    unittest.main()
    