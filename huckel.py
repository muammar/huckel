#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = "Muammar El Khatib"
__copyright__ = "Copyright 2014, Muammar El Khatib"
__credits__ = [""]
__license__ = "GPL"
__version__ = "3"
__maintainer__ = "Muammar El Khatib"
__email__ = "muammarelkhatib@gmail.com"
__status__ = "Development"
"""
"""
This is a python program that takes your MOLPRO output file, and from the
Cartesian coordinates, it forms a Huckel hamiltonian matrix to then give you
the eigenvalues to be plotted against the normalized eigenvalues ordinal
numbers as showed in `[1]`.

1.  M. El Khatib, S. Evangelisti, T. Leininger, and G. L. Bendazzoli, Phys.
    Chem. Chem. Phys., 2012, 14, 15666–76.
"""

"""
The name of the output is readed from the prompt
"""
import sys
len(sys.argv)
input=str(sys.argv[1])

# Comma separated values module is loaded
import csv
import numpy as np

print ('')
print ('Does your molecule have different inter atomic distances for the carbon atoms? [Default answer: no]')
yes = set(['yes','y', 'ye', 'Yes', 'Ye', 'Y'])
answer=raw_input()
if answer in yes:
    print ('Please enter the interval of distances in the format: lower, maximum')
    intervalo=raw_input().split(",")
    print ('The requested interval is: ' + str(intervalo))
else:
    print ('Enter the only internuclear value of your molecule:')
    inter=raw_input()
    print ('The requested value is: ' + str(inter))

"""
Atom list to be removed
"""
atomlist=[]
print ('Would you like to delete some carbon atoms? [Default answer: no]')
yesal = set(['yes','y', 'ye', 'Yes', 'Ye', 'Y'])
answeral=raw_input()
if answeral in yesal:
    print ('Please enter the number of the desired atoms to be deleted')
    atoml=[raw_input().split(",")]
    print ('The requested atoms to be deleted are: ' + str(atoml))
    atomln=np.asarray(atoml,dtype=np.int32)
    atomlist=atomln-1

"""
In this part of the code, we take the coordinates of the molecule from the
MOLPRO output file and then we dump its content in outfile.
"""
with open(input) as infile, open('coord','w') as outfile:
    copy = False
    for line in infile:
        if line.strip() == "NR  ATOM    CHARGE       X              Y              Z":
            copy = True
        elif line.strip() == "Bond lengths in Bohr (Angstrom)":
            copy = False
        elif copy:
            outfile.write(line)

outfile.close()

"""
Now we create csv
"""
with open('coord') as fr, open('coordv', 'w') as fw:
    for line in fr:
        fw.write(','.join(line.strip().split()) + '\n')

# Unneeded columns are deleted from the csv
input = open('coordv', 'rb')
output = open('coordvout', 'wb')
writer = csv.writer(output)
for row in csv.reader(input):
    if row:
        writer.writerow(row)

input.close()
output.close()

with open('coordvout','rb') as source:
    rdr= csv.reader( source )
    with open('coordbarray','wb') as result:
        wtr= csv.writer(result)
        for r in rdr:
            # Here, we strip out atoms different from C
            if not r[1].startswith('H'):
                wtr.writerow( (r[3], r[4], r[5]) )

# Import csv files to matrices in numpy.
from numpy import genfromtxt
coordmatrix = genfromtxt('coordbarray', delimiter=',')

print ('')
print ('Coordinate array')
print ('')
print(coordmatrix)

"""
In this section we erase atoms from atomlist if they were introduced at run time
"""

coordmatrix=np.delete(coordmatrix, (atomlist), axis=0) #Row

print ('')
print ('Coordinate after deletion of saturated carbons')
print ('')
print(coordmatrix)


"""
Now, the distances between two points in the 3D arrays are calculated using
scipy and cdists.
"""
import scipy.spatial as sp
distances=sp.distance.cdist(coordmatrix,coordmatrix, 'euclidean')

print ('')
print ('Distances between atoms')
print ('')
print distances

print ('')
hshape=distances.shape
print ('The Huckel Hamiltonian Matrix of shape ' + str(hshape) + ' is printed below:')
print ('')
#for x in np.nditer(distances, flags=['external_loop'], order='F'):
#    print x

#distances[np.isclose(distances, 0)]  = 1
if answer in yes:
    distances[distances > float(intervalo[1])] = 0
    distances[(distances > float(intervalo[0])) * (distances < float(intervalo[1]))] = -1
else:
    distances[distances > float(inter)] = 0
    distances[np.isclose(distances, float(inter))]  = -1

print distances
print ('')

"""
Calculation of Eigenvalues and Eigenvectors using scipy
"""
hshape=distances.shape
from scipy import linalg as LA
e_vals, e_vecs = LA.eigh(distances)

idx = e_vals.argsort()
idxv = e_vecs.argsort()

print ('indices')
print (idx)
print (idxv)
print ('evals')
print (e_vals[idx])
print ('')
print ('evecs')
print (e_vecs[:,idx])
print ('')
"""
A counter is created in the loop, and for each iteration such index is divided
by the shape of the columns of the Huckecl matrix which is squared (M,N); M=N.
With this, we normalized the X axis for the later plot of the values.
"""
counter=0
with open('huckel.dat','w') as hout:
    for i in e_vals:
        norm=counter+1
        norma=norm/float(hshape[0])
        print norma,i
        hout.write(str(norma)+ ' ' + ' ' +  str(i) + '\n')
        counter += 1


"""
In this part, files are cleaned. If you want to let them, then you can comment
all this section.
"""
import os
# Files related to the coordinates
os.popen('rm -f coord coordbarray coordv coordvout')
