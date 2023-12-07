print('Hello World')
#this is a single line comment

"""
This is a comment
written in
more than just one line 
also known as multi-line.
"""
x=5
print(x)

temp = "5 degrees"
cel = 0
fahr = float(temp)
cel = (fahr - 32.0) * 5.0 / 9.0
print(cel)

#You can assign multiple values to multiple variables:
x , y , z = "Banana" , "Mangoes" , "Avocadoes"
print(x)
print(y)
print(z)
#Global variables:can be used by everyone:
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#Data type :
x = 5
print(type(x))

#Python numbers:
#int:-
"""A whole number"""

V = 5
I = 14
O = 2
print(type(V))
print(type(I))
print(type(O))

#float:-
"""A positive Number positive or negative with a decimal 
Float can also be scientific numbers with an "e" 
to indicate the power of 10."""
V = 5.34
print(type(V))

#one with "e";
V = 5.34e6
print(type(V))

#complex:-
"""Complex numbers are written with a
 "j" as the imaginary part:"""

I =5j
print(type(I))

#to convert from one type to the other:

v= 2 #int
i= 3.3 #float
c=5e3 #float
t=7j #Complex

#convert float to int:

a= int(i)

#convert complex to int:

b= int(t)

print(a)
print(b)

"""
Python does not have a random() function to make a random number,
 but Python has a built-in module called
 random that can be used to make random numbers:
"""
import random
print(random.randrange(1, 10)) #this will print random number from 1 to 10
