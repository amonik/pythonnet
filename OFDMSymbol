#!/usr/bin/env python #allows you to run from command line

from scipy import *
from numpy import *
import numpy as np #This a Alias 'np' allows you to access the numpy libary faster
from random import * #if you import everything you may have conflicts with the name
from cmath import *
from gnuradio import *


class OFDMsubframe:
	"""docstring for ClassName"""
	def __init__(self, SymbolsPerSubFrame, NumBitsPerSymbol, N):
			
		self.SymbolsPerSubFrame = SymbolsPerSubFrame
		self.NumBitsPerSymbol = NumBitsPerSymbol
		self.N = N

if __name__ == '__main__':
	obj = OFDMsubframe(12, 2, 64)
	
			

numbers = zeros(obj.SymbolsPerSubFrame*(obj.N-2)*obj.NumBitsPerSymbol)
binarySeq = [randint(0,1) for x in range(len(numbers))] 
o = np.matrix([2,1])
mat = o.T #transpose of matrix
k = range(1,(len(binarySeq) / obj.NumBitsPerSymbol) + 1) 


b = [(binarySeq[x], binarySeq[x+1])*mat for x in range(len(k))]

b = resize(b,(744))
b = list(b)

for i in range(len(b)):
    if b[i] == 0:
        b[i] = exp(1j*(1*pi/4)*1)
    elif b[i] == 1:
        b[i] = exp(1j*(1*pi/4)*3) 
    elif b[i] == 2:
        b[i] = exp(1j*(1*pi/4)*5) 
    elif b[i] == 3:
        b[i] = exp(1j*(1*pi/4)*7) 
  
b = array(b)
y = split(b,obj.SymbolsPerSubFrame) 
timesym = ifft(y[:12],obj.N)	
i = zeros(12)
timesubframe = [append(timesym[j,48:64],timesym[j]) for j in range(len(i))]
