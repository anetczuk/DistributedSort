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


import sys
import time
import argparse 
import logging
from dsort.master import Master
from dsort.nmerge import NMerge




## ============================= main section ===================================


if __name__ != '__main__':
    sys.exit(0)


parser = argparse.ArgumentParser(description='Presentation of N-merge sorting algorithm in distributed environment')
#parser.add_argument('--algorithm', "-a", action='store', required=False, default="NM", choices=["NM"], help='Algorithm: NMerge' )
parser.add_argument('-N', action='store', required=False, default=5, help='Size of worker' )
parser.add_argument('-K', action='store', required=False, default=5, help='Number of workers' )
 
 
args = parser.parse_args()
 

logging.basicConfig(level=logging.DEBUG)



try:
    starttime = time.time()
    
    N = int(args.N)
    K = int(args.K)
    
    master = Master(K, N)
    master.randomizeNodes()
    
    print "Before sorting"
    master.printData()
    
    merge = NMerge()
    merge.sortNaive(master)
    
    print "After sorting"
    master.printData()
    
    timeDiff = (time.time()-starttime)*1000.0
    print "Calculation time: {:13.8f}ms".format(timeDiff)
finally:
    pass
