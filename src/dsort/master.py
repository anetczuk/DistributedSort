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
import random


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
        
        self.nodesNum = K
        self.nodeSize = N
        self.nodes = [ Node( self.nodeSize ) for _ in range( self.nodesNum ) ]
        self.buffer = [0]*self.nodesNum

        
    def randomizeNodes(self):
        dataLen = self.nodesNum*self.nodeSize
        randomData = random.sample( xrange(0, dataLen), dataLen)
        for n in self.nodes:
            randomSlice = randomData[:self.nodeSize]
            n.data = randomSlice
            del randomData[:self.nodeSize]


    def nodeData(self, nodeIndex, dataIndex):
        return self.nodes[nodeIndex].getData(dataIndex)


    def setNodeBuffer(self, nodeIndex, dataIndex, value):
        self.nodes[nodeIndex].buffer[dataIndex] = value


    def sortNodesParallel(self):
        ## order parallel sorting in each node
        for n in self.nodes:
            n.orderSort()
        ## wait for nodes to finish sorting operation
        for n in self.nodes:
            n.wait()


    def sortBuffer(self):
        self.buffer.sort()
    
            
    def printData(self):
        for i in range(len(self.nodes)):
            n = self.nodes[i]
            print "Node {}: {}".format(i, n.data)

    