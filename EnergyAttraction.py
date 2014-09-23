#!/usr/bin/env python


from numpy import *
from math import *
import pylab as plt
import numpy as np

start = 0.05
stop = 1.05
step = 0.05

r = arange(start,stop,step) 

#["%g" % x for x in r] # print r

xEA = [-1.436] * len(r) #creates n array of -1.436


EA  = divide(xEA,r) # divides the two array. #EA Engery Attraction

#print EA

xER = [5.86e-6] * len(r)

ER = divide(xER,((r**9))) #r is raised to power of 9

["%g" % x for x in ER]

ET = [sum(x) for x in zip(EA, ER)] #add two arrays


plt.title('Energy Attraction, Energy Repulsion, Energy Total of K+ and Cl-')
plt.xlabel('Number of r')
plt.ylabel('Energy')
plt.axis([0, 1.0, -6, 6])
#plt.text(0.1,0.5, 'Energy Repulsion (ER)')
plt.plot(r, EA ,'b^')
plt.plot(r, ER, 'g--')
plt.plot(r, ET,'r--')
plt.show() 

##3(c)

#### Calculate r0 ############################
A = -xEA[0]
B = xER[1]
n = 9
x = (A/(n*B))
y = (1.0/(1.0-n))
r0 = x**y #r0 is separation distance at the 
#minimum of the potential energy curve.

##### Calculate E0 #####################

EAy = -(A / r0)
ERy = B / x**(n*y)

E0 = EAy + ERy

print 'Separation distance at the minimum of the potential energy curve: %s' %r0
print "\n"
print 'Your E0 value is: %e' % E0
