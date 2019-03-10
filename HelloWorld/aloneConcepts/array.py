from array import *

vals = array('i', [5,10,15,40])
print(vals)
print(vals.buffer_info())

for i in range(3):
    print(' ----- ', vals[i])

newArray = array(vals.typecode, (a*a for a in vals))

for e in newArray:
    print(newArray)

# https://docs.python.org/2/library/array.html
# vals = array('I', [5,10, -8 ,15,40])
# print(vals) #shoud bring me an error...