# Python Program to calculate the square root for positive numbers

# Note: change this value for a different result
num = 8 

num_sqrt = num ** 0.5
print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))


# Find square root of real or complex numbers
# Importing the complex math module
import cmath
num = 1+2j

num_sqrt = cmath.sqrt(num)
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))
