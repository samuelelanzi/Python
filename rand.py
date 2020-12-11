import numpy.random as rnd
from array import array
# from random import *

x = array('d')

# print(random())
# print(randint(1, 10))

x = rnd.uniform(low = 0.0, high = 1.0, size = 100)

for i in range (len(x)):
    print(x[i])