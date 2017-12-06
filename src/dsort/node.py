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


import random


class Node(object):
    '''
    Node class
    '''


    def __init__(self, N):
        '''
        Constructor:
        N - number of elements
        '''
        self.dataSize = N
        self.data = [0]*N           ## data buffer
        self.buffer = [0]*N         ## input buffer
        
        
    def randomizeData(self, startValue=0):
        self.data = random.sample( xrange(startValue, startValue+self.dataSize), self.dataSize)
        
        
    def popFirst(self):
        self.data.append( self.data[ self.dataSize-1 ] )    ## repeat greatest element
        return self.data.pop(0)
    
    
    def setLast(self, val):
        self.data[ self.dataSize-1 ] = val
    
    
    def sortData(self):
        self.orderSort()
        self.wait()

        
    def orderSort(self):
        self.data.sort()


    def wait(self):
        '''
        Wait for node to finish it's current task.
        '''
        pass        ## do nothing, just simulate waiting

