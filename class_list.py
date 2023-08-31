#Methode how to use the list and its types

#mylist = ["apple" , "banana" , "cherry"]

#Lists are used to store multiple items in a single variable.

#Lists are created using square brackets:

thislist = ["apple", "banana", "cherry"]
print(thislist)

#List Items
#List items are ordered, changeable, and 
# allow duplicate values.

#List items are indexed, the first item has index [0], 
# the second item has index [1] etc.

#Ordered
#When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

#If you add new items to a list, the new items will 
#be placed at the end of the list.

#Lists allow duplicate values:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#List Length
#Print the number of items in the list:

thislist = ["apple", "banana", "cherry", "mango"]
print(len(thislist))

#List Items - Data Types
#String, int and boolean data types:

list1 = ["apple", 'banana', 'cherry']
list2 = [10, 20, 30, 40, 50, 8]
list3 = [False, True, False]

print(list1)
print(list2)
print(list3)


#A list can contain different data types:
#A list with strings, integers and boolean values:

list1 = ["abc" , 34, True, 40, "male", 'female']

print(list1)

# type()
# What is the data type of a list?

mylist = ['apple', 'banana', 'cherry']
print(type(mylist))

#The list() Constructor
#Using the list() 
#constructor to make a List:
#it usually used when initialize any software

thislist = list(('apple', 'banana', 'cherry', )) #note the double round-brackets
print(thislist)

#Access Items
#Print the second item of the list:

thislist = ['apple', 'banana', 'cherry']
print(thislist[2])






