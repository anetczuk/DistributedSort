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

from dsort.node import Node


class Master(object):
    '''
    Master class
    '''


    def __init__(self, K, N):
        '''
        Constructor
        K - number of nodes
        N - number of elements in single node
        '''
        
        self.nodeSize = N
        self.nodes = [ Node(N) for _ in range(K) ]
        self.buffer = [0]*K
        
    def randomizeNodes(self):
        startVal = 0
        for n in self.nodes:
            n.randomizeData(startVal)
            startVal += self.nodeSize
            
    def printData(self):
        for i in range(len(self.nodes)):
            n = self.nodes[i]
            print "Node {}: {}".format(i, n.data)
