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

#Negative Indexing
#-1 refers to the last item, 
# -2 refers to the second last item etc.

#Print the last item of the list:

thislist = ['apple', 'banana', 'cherry']
print(thislist[-2])

#Range of Indexes

#You can specify a range of indexes by 
#specifying where to start and where to end the range.

#When specifying a range, the return value will be
# a new list with the specified items.

#Return the third, fourth, and fifth item:

thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thislist[2:5])

#By leaving out the start value, 
# the range will start at the first item:

thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thislist[:6])

#By leaving out the end value, the range 
# will go on to the end of the list:

#This example returns the items 
# from "cherry" to the end:

thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thislist[2:])

#Range of Negative Indexes

#Specify negative indexes if you want to start 
# the search from the end of the list:

#This example returns the items from "orange" 
#(-4) \ to, but NOT including "mango" (-1):

thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thislist[-4:-1])

#Check if Item Exists
#To determine if a specified item is 
#present in a list use the in keyword:

thislist = ['apple', 'banana', 'cherry']
if 'apple' in thislist:
   print("yes, 'apple' is in the fruits list")
   




