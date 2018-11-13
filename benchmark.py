__license__ = 'Nathalie (c) EPITA'
__docformat__ = 'reStructuredText'
__revision__ = '$Id: prefixTrees.py 2018-02-14'

"""
Prefix Trees homework
2018
@author: login
"""


from algopy import tree
from test import *

################################################################################
## MEASURES
       
def countwords(T):
	acc = 0
	if T.key[1]:
		acc+=1
	for child in T.children:
		acc += countwords(child)
	return acc
#print(countwords(Tree1))

def __longestwordlength(T, dept=0, maxdept=0):
	if T.key[1] and dept > maxdept:
		maxdept = dept
	for child in T.children:
		temp = __longestwordlength(child, dept+1,maxdept)
		maxdept = max(maxdept, temp)
	return maxdept

def longestwordlength(T):
		return __longestwordlength(T)
#print(longestwordlength(Tree1))

def __averagelength(T, dept=0):
	tot = 0

	if T.key[1]:
		tot += dept
	for child in T.children:
		tot += __averagelength(child, dept+1)
	return tot

def averagelength(T):
		return __averagelength(T)/countwords(T)
print(averagelength(Tree1))


