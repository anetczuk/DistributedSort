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



class NMerge(object):
    '''
    Master class
    '''


    def __init__(self):
        '''
        Constructor
        K - number of nodes
        N - number of elements in single node
        '''
        
        self.master = None
        self.bufferMinIndex = -1
        self.nodeDataIndex = []


    def sortNaive(self, master):
        '''
        NMerge algorithm. Description: https://en.wikipedia.org/wiki/Merge_algorithm
        '''
    
        if master.nodeSize < 1:
            ## nothing to sort
            return
        
        self.master = master
            
        self.master.sortNodesParallel()
        
        if master.nodesNum <= 1:
            ## only one node -- already sorted
            return
            
        ## init master buffer        
        self.initMasterBuffer()
        
        for n in xrange(0, self.master.nodesNum):
            for i in xrange(0, master.nodeSize):
                self.findBufferMin()
                master.setNodeBuffer(n, i, master.buffer[self.bufferMinIndex])
                self.completeTheBuffer()

            
    def initMasterBuffer(self):
        for i in xrange(0, self.master.nodesNum):
            self.master.buffer[i] = self.master.nodeData(i, 0)
        self.nodeDataIndex = [0] * self.master.nodesNum
        
    
    def findBufferMin(self):
        buffMinIndex = -1
        for i in xrange(0, self.master.nodesNum):
            if self.nodeDataIndex[i] >= self.master.nodeSize:
                ## no data in node
                continue
            if buffMinIndex < 0:
                ## first node
                buffMinIndex = i
                continue
            ## compare data
            if self.master.buffer[i] < self.master.buffer[buffMinIndex]:
                buffMinIndex = i
        self.bufferMinIndex = buffMinIndex
        
        
    def completeTheBuffer(self):
        self.nodeDataIndex[ self.bufferMinIndex ] += 1
        currIndex = self.nodeDataIndex[ self.bufferMinIndex ]
        if currIndex < self.master.nodeSize:
            self.master.buffer[self.bufferMinIndex] = self.master.nodeData(self.bufferMinIndex, currIndex )
        
        

