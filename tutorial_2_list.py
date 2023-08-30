#learn list 

#Lists are used to store multiple items in a single variable.

#example

thislist = ["apple", "banana", "cherry"]
print(thislist)

#List items are ordered, changeable, and allow duplicate values.

#List items are indexed, the first item has index [0], the second item has index [1] etc.

#Ordered

#When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

#If you add new items to a list, the new items will be placed at the end of the list.

#Changeable
#The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

#Allow Duplicates
#Since lists are indexed, lists can have items with the same value:

thislist = ["apple", "cherry", "banana", "apple", "cherry"]
print(thislist)

#List Length

#To determine how many items a list has, use the len() function:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#List Items - Data Types
#list items can be of any data type:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

#A 1 list can contain different data types:

list1 = ["sam", 40, True, 30, "male"]

print(list1)

#type()
#From Python's perspective, lists are defined as objects with the data type 'list':

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#The list() Constructor
#It is also possible to use the list() constructor when creating a new list.

#note the double round-brackets 

thislist = (("banana", "cherry", "apple"))
print(thislist)

#Python Collections (Arrays)
#There are four collection data types in the Python programming language:

#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.

#Access Items

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Negative Indexing
#Negative indexing means start from the end

thislist = ["apple", "banana", "cherry"]
print(thislist[-2])

#Range of Indexes
#You can specify a range of indexes by specifying where to start and where to end the range.

#When specifying a range, the return value will be a new list with the specified items.
thislist = ["apple", "banana", "cherry", "kiwi", "orange", "melon", "mango"]
print(thislist[2:5])

#This will return the items from position 2 to 5.

#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included

#This example returns the items from the beginning to, but NOT including, "orange":
thislist = ["apple", "banana", "cherry", "kiwi", "orange", "melon", "mango"]
print(thislist[:4])

#This example returns the items from "cherry" to the end:
thislist = ["apple", "banana", "cherry", "kiwi", "orange", "melon", "mango"]
print(thislist[2:])

#This example returns the items from "kiwi" (-4) to, but NOT including "mango" (-1):

thislist = ["apple", "banana", "cherry", "kiwi", "orange", "melon", "mango"]
print(thislist[-4:-1])

#Check if Item Exists

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("yes, 'apple' is in the fruits list")

  #Change Item Value
#To change the value of a specific item, refer to the index number:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "kiwi"
print(thislist)

#Change a Range of Item Values
#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


#Change the second value by replacing it with two new values:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#insert Items
#To insert a new list item, without replacing any of the existing values, we can use the insert() method.

#The insert() method inserts an item at the specified index:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "watermelon")
print(thislist)

#Append Items
#To add an item to the end of the list, use the append() method:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Extend List
#To append elements from another list to the current list, use the extend() method.

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Remove Specified Item

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Remove Specified Index

thislist = ["apple", "banana", "cherry"]
thislist.pop(2)
print(thislist)

#If you do not specify the index, the pop() method removes the last item.

#Clear the List
#The clear() method empties the list.

#The del keyword can also delete the list completely.


q?
#Loop Through a List
#You can loop through the list items by using a for loop:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

q?

  #Loop Through the Index Numbers
#You can also loop through the list items by referring to their index number.

#Use the range() and len() functions to create a suitable iterable.

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

  