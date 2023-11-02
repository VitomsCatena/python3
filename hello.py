print('Hello World')
#this is a single line comment

"""
This is a comment
written in
more than just one line 
also known as multiline.
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
#float:-
"""A positive Number positive or negative with a decimal 
Float can also be scientific numbers with an "e" 
to indicate the power of 10."""

#complex:-
"""Complex numbers are written with a
 "j" as the imaginary part:"""