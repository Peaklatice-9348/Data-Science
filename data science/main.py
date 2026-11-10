import numpy

list = list(range(100,201))
print(type(list))

array = numpy.array(list)
print(array)
print(type(array))

array+=10

print(array)

array2 = numpy.arange(1,268,2,dtype=numpy.int8)
print(array2)