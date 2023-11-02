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