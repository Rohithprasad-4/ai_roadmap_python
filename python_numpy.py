#Numpy
##1D array
import numpy as np
lst=[1,2,3,4]
a=np.array(lst)
print(a)
b=a.shape
print(b)#you will get only one value because its 1D 
c=type(a)#which delacre the type of array
print(c)
##2D array
lst1=[1,2,3,4,5]
lst2=[2,3,4,5,7]
lst3=[3,4,5,6,7]
d=np.array([lst1,lst2,lst3])
print(d)
e=d.shape
print(e)
z=lst[3]#indexing
print(z)
y=lst[2]=12
print(lst)
x=lst[1:]
print(x)
e=lst[1:4]
print(e)
q=lst[:-1]
print(q)
r=lst[::-1]#print the array reverse
print(r)
s=lst[::-2]#its skips two numbers from last
print(s)
p=d[:,1]#prints first column
print(p)
f=d
##
print(d)
##reshape
w=d.reshape(5,3)
print(w)
##mechanisms to create an array
o=np.arange(1,11,1).reshape(2,5)
print(o)
q=np.ones((5,3))#matric full of ones
print(q)
x=np.zeros((5,3))#matric full of zeros
print(x)
t=np.zeros_like((5,3))
print(t)
h=np.random.randint(0,100,5)#creating random
print(h)
l=np.random.randn(5,6)#creating using noraml distubution
print(l)