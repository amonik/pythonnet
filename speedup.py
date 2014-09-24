#Code graphs the speedup of system through parellel processing

#!/usr/bin/env python

from numpy import *
from math import *
import pylab as plt
import numpy as np


###creating fuction that can accept any f or p and output the answer. 
def s(f, p, sp=[]):
	sp = (100.00 / ((100.00-p) + (p / (1 + (f/100.00))))) #speed up equation
	return sp


y100 = [(s(100,20)),(s(100, 80))] # problem i and ii. This is f at 100
y100 = ['%.2f' % elem for elem in y100] #changes every item to float
y100 = map(float, y100) # item above make is a float string, so this make it a float number with percision of 2
y300 = [(s(300,10)),(s(300, 60))] # problem iii and iv. This is f at 300
y300 = ['%.2f' % elem for elem in y300]
y300 = map(float, y300)

x100 = [20,80]
x300 = [10,60]

#prints the results.
print "(1a)  The overall speedup:"
print 'i. f = 100, p = 20: = %s' %y100[1]
print 'ii. f = 100, p = 20: = %s' %y100[0]
print 'iii. f = 300, p = 60: = %s' %y300[1]
print 'iv. f = 300, p = 10: = %s' %y300[0]


#############Graph and code of f at 100 and 300 from 0 to 10.#######################
f1 = 100
f2 = 300
p1 = range(0, 110, 10)
pprime = zeros(len(p1))
oldtime = zeros(len(p1))
newtime = zeros(len(p1))
speedup = zeros(len(p1))
pprime2 = zeros(len(p1))
oldtime2 = zeros(len(p1))
newtime2 = zeros(len(p1))
speedup2 = zeros(len(p1))
for a in range(len(p1)):
	pprime[a] = (p1[a]*100) / (100 + f1) #speed up equation, another way to compute it.
	oldtime[a] = (100 - p1[a]) + p1[a]
	newtime[a] = (100 - p1[a]) + pprime[a]
	speedup[a] = oldtime[a] / newtime[a]

	pprime2[a] = (p1[a]*100) / (100 + f2)
	oldtime2[a] = (100 - p1[a]) + p1[a]
	newtime2[a] = (100 - p1[a]) + pprime2[a]
	speedup2[a] = oldtime2[a] / newtime2[a]

speedup = ['%.2f' % elem for elem in speedup]
speedup = map(float, speedup)

speedup2 = ['%.2f' % elem for elem in speedup2]
speedup2 = map(float, speedup2)

###plots####
plt.title('(1b) Amdahls Law Graph of speedup functions for f = 100 and f = 300')
plt.xlabel('The new feature (p%)')
plt.ylabel('The speedup (sp)')
plt.text(20.397, 0.88, 'f = 100, p = 20')
plt.text(78.23, 3.3, 'f = 300')
plt.text(84.0, 2.0, 'f = 100')
plt.text(9.47, 1.32, 'f = 300, p = 10')
plt.text(46.16, 2.07, 'f= 300, p = 60')
plt.text(77.17,1.39, 'f = 100, p = 80')
plt.axis([0, 100, 0, 4])
plt.plot(x100,y100,'b^')
plt.plot(p1, speedup)
plt.plot(x300,y300, 'g^')
plt.plot(p1, speedup2)
plt.show()

