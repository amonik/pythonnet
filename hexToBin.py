#!/usr/bin/env python
'''
This code takes in a Hex file and changes the data to binary stirngs.

'''

from numpy import *
a = open('OFDM.dat') #opens the file
lines = a.readlines() # reads the lines in the file and puts them in lines
A = array(lines) # creates an array that inlcudes the lines 
B = bytearray(A) # breaks into bytes

D = byte(B) #changes the hex to list of bytes
E = filter(lambda a: a != 0, D) #removes the zeros 
C = range(len(E)) # creates an array of size B
bin8 = lambda x : ''.join(reversed( [str((x >> i) & 1) for i in range(8)] ) )
for i in range(len(E)): #for loop 
    C[i]=bin8(E[i])





