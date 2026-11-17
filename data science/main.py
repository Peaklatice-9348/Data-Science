import numpy

list = list(range(100,201))
print(type(list))

array = numpy.array(list)
print(array)
print(type(array))

array+=10

print(array)

array2 = numpy.arange(1,268,2,dtype=numpy.uint8)
print(array2)

array3 = numpy.linspace(0,20,11)
print(array3)

num = numpy.random.randint(0,2,1000)
print(num)

array4 = numpy.ones((2,2))
print(array4)

array5 = numpy.zeros((2,2))
print(array5)

print(array4.ndim)
print(array4.shape)
print(array4.size)

array6 = num.reshape((10,10,10))
print(array6)

array7 = numpy.arange(0,20,1,int)
print(array7)

array8 = numpy.random.permutation(array7)
print(array8)

array9 = numpy.random.permutation(array7.reshape((4,5)))
print(array9)

array10 = numpy.sort(array8)
print(array10)
array11 = numpy.array([1,3,5,2,9,7,3,3,4],int).reshape((3,3))
#axis=1 is row rise, axis=0 is column wise
print(array11,end='\n\n')
print(numpy.sort(array11),end='\n\n')
print(numpy.sort(array11,axis=0),end='\n\n')

print(array7[0:20:2])
#conditional slicing
print(array7[(array7%3==0)&(array7%5==0)])