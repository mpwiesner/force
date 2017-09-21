#!/usr/bin/python
import numpy as np
import sys
np.set_printoptions(threshold=np.nan)
import csv
import math
import matplotlib.pyplot as plt
from numpy import zeros,abs,multiply,array,reshape

name="test"     							   #The starting number of images to run on

print "loading ", name

m = np.loadtxt(name, skiprows=0)

ra=m[:,0]
dec=m[:,1]
u=m[:,2]
g=m[:,3]
r=m[:,4]
i=m[:,5]
z=m[:,6]

plt.plot(ra, dec, linewidth=1.0)

plt.xlabel('RA (Degrees)')
plt.ylabel('DEC (Degrees)')
plt.axis([190,191,-1.25,1.25])
	
plt.show()



