#important points for differntiate list

# 1.list is used to store multiple data
#2. list take dublicate values.
#3. List items are ordered, changeable, 
#and allow duplicate values.
#4  Lists are created using 
#square brackets:


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

#Change Item Value
#To change the value of a specific item, 
# refer to the index number:


thislist = ['apple', 'banana', 'cherry']
thislist[1] = 'blackcurrant'
print(thislist)

#Change a Range of Item Values

#To change the value of items within a specific range,
# define a list with the new values, and 
# refer to the range of index numbers 
# where you want to insert the new values:

thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango']
thislist[1:3] = ['blackcurrant', 'watermelon']
print(thislist)

#If you insert more items than you replace, the new items will be 
# inserted where you specified, and the 
# remaining items will move accordingly:
#Change the second value by replacing it with two new values:

thislist = ['apple', 'banana', 'cherry']
thislist[1:2] = ['blackcurrant', 'watermelon']
print(thislist)

#Note: The length of the list will change 
# when the number of items inserted does 
#not match the number of items replaced.

#If you insert less items than you replace, 
# the new items will be inserted where you specified, 
# and the remaining items will move accordingly:

#Change the second and third 
# value by replacing it with one value:

thislist = ['apple', 'banana', 'cherry']
thislist[1:3] = ['watermelon']
print(thislist)

#Insert Items
#To insert a new list item, without 
#replacing any of the existing values, 
# we can use the insert() method.
#The insert() method inserts 
# an item at the specified index:
#Insert "watermelon" as the third item:

thislist = ['apple', 'banana', 'cherry']
thislist.insert(2, 'watermelon')
print(thislist)

#Note: As a result of the example above, 
# the list will now contain 4 items.

#Append Items
#To add an item to the end of the list, 
# use the append() method:
#to append an item:

thislist = ['apple', 'banana', 'cherry']
thislist.append('orange')
print(thislist)

#Extend List
#To append elements from another 
# list to the current 
# list, use the extend() method.

#Add the elements 
# of tropical to thislist:

thislist = ['apple', 'banana', 'cherry']
tropical = ['mango', 'pinaple', 'papaya']
thislist.extend(tropical)
print(thislist)


#Add Any Iterable
#The extend() method does not have to append 
# lists, you can add any iterable object 
# (tuples, sets, dictionaries etc.).

#Add elements of a tuple to a list:

thislist = ['monday', 'thuesday', 'wednesday']
thistuple = ('thursday', 'friday')
thislist.extend(thistuple)
print(thislist)

#Remove Specified Item
#The remove() method 
# removes the specified item.

#Remove "tuesday":

thislist = ['monday', 'tuesday', 'wednesday']
thislist.remove('tuesday')
print(thislist)

#If there are more than one item with the specified value, the 
# remove() method removes the first occurance:

#Remove the first occurance of "monday":

thislist = ['tuesday', 'wednesday', 'monday', 'thursday', 'friday', 'monday']
thislist.remove('monday')
print(thislist)

#Remove Specified Index
#The pop() method removes the 
# specified index.
#Remove the second item:

thislist = ['january', 'february', 'march', 'april']
thislist.pop(1)
print(thislist)

#If you do not specify the index, t
#he pop() method removes the last item.

#Remove the last item:

thislist = ['january', 'february', 'march']
thislist.pop()
print(thislist)

#The del keyword 
#also removes the specified index:
#Remove the first item:

thislist = ['monday', 'tuesday', 'wednesday']
del thislist[0]
print(thislist)

#The del keyword can also 
#delete the list completely.

#Delete the entire list:
thislist = ['monday', 'tuesday', 'wednesday']
del thislist

#Clear the List
#The clear() method empties the list.
#The list still remains, 
# but it has no content.

#clear the list content

thislist = ['january', 'february', 'march']
thislist.clear()
print(thislist)

#Loop Through a List

#You can loop through the 
# list items by using a for loop:

#Print all items in the list, one by one:

thislist = ['monday', 'thuesday', 'wednesday']
for x in thislist:
   print(x)

#Loop Through the Index Numbers
#You can also loop through the list items 
#by referring to their index number.

#Use the range() and len() functions to 
# create a suitable iterable.

thislist = ['monday', 'thuesday', 'wednesday']
for i in range(len(thislist)):
   print(thislist[i])












