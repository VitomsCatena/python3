#SET
----------------------------------------------------------------------------------------------------------------------------------------------------
#Is a collection of unordered, unchangable and unindexed variables. opposed to tuples.

SetType= {"food" ,"soda" ,"water"}
print(SetType)
----------------------------------------------------------------------------------
#to add an Item we use
add()

----------------------------------------------------------------------------
#to remove set item:
----------------------------------------------------------------------------

#remove()

    thisset = {"apple", "banana", "cherry"}

thisset.remove("banana") #this will remove banana from the list

print(thisset)
-------------------------------------------------------------------------

#discard()

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana") #banana will be discarded

print(thisset)
-----------------------------------------------------------------------

#clear()
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
---------------------------------------------------------------------

#del()
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)
---------------------------------------------------------------------
#pop()
hisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
