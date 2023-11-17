#int
v = 45

#float

i= 4.5

#complex

c = 5j


print(v)
print(i)
print(c)

#change from one type to the other:

A= int(c) # will change complex to interger.


print(type(A))

#To print random numbers
import random

print(random.randrange(1 , 200))

#python casting

x = int(1)   # x will be 1
y = int(4.8) # y will be 4
z = int("7") # z will be 7

#for float:

x = float(3) # x will be 3.0
y = float ("23") # will be 23

#for  strings

x = str('23') #will be '23'
y = str(2.9) # will be '2.9'

#to get string lenght:

a = "I am ok"
print(len(a))
#The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

birth_year = input ("Enter your birth year:)
int(birth_year)
age = 2023#current year - int(birth_year) 
"""
for instance if the input is 2002 the output
will be 21
"""
