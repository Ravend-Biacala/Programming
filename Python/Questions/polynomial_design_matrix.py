# EXERCISE: The 'polynomial design matrix' cell
#
# Your first exercise is to implement the function 'polynomial_design matrix'
# in the module file lab_1.py. See the instructions there. Evaluate this cell
# to call that function, to check that it's working.
# You should get a matrix (array of arrays) in which each row contains successive powers of each element of the input:
# example: print (lab_1.polynomial_design_matrix(np.array ([2,4,3]), 3))
# [[ 1.  2.  4.  8.]
#  [ 1.  4. 16. 64.]
#  [ 1.  3.  9. 27.]]
# print (lab_1.polynomial_design_matrix(np.array ([2,4,3]), 3))

import numpy as np 

def polynomial_design_matrix(matrix, num):
    lst = []
    for i in matrix:
        lst.append(power(i,num))
    return np.array(lst)

def power(a,b): 
    p = 1.
    lst = [p]
    for i in range(0,b): 
        p *= a 
        lst.append(p)
    return lst 
    
print(polynomial_design_matrix(np.array([2,4,3]),3))
 
# Resources and Links
# https://stackoverflow.com/questions/2891790/pretty-print-a-numpy-array-without-scientific-notation-and-with-given-precision
# https://www.quora.com/How-do-I-make-a-number-an-exponent-of-another-in-Python-without-using-the-inbuilt-%E2%80%98**%E2%80%99-or-the-%E2%80%98math-pow%E2%80%99
# https://stackoverflow.com/questions/1019740/speed-of-calculating-powers-in-python
# https://www.digitalocean.com/community/tutorials/how-to-convert-data-types-in-python-3
# https://www.w3schools.com/python/numpy/numpy_array_iterating.asp
# print(np.array([2.0,4.0,3.0], ))

# x = np.random.random(10)
# print(x)
# print(power(3,3))
