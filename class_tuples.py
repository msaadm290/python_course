# # 1.Tuple is used to store multiple data
# #2. tuple is also take dublicate values.
# #3. Tuples are unchangeable, meaning that 
# # we cannot change, add or remove 
# # items after the tuple has been created.
# #4 Tuple are created using 
# #round brackets:
# # tuple always use(",") after one item to indentify its a tuple.

# #Tuple
# #Tuples are used to store multiple 
# #items in a single variable.

# #Tuple is one of 4 built-in data types 
# #in Python used to store collections of data, 
# #the other 3 are List, Set, and Dictionary, 
# #all with different 
# #qualities and usage.

# #A tuple is a collection which is ordered and unchangeable.
# #Tuples are written with round brackets.

# #create a tuple:

# thistuple = ('thuesday', 'wednesday', "thursday")
# print(thistuple)

# #Tuple Items

# #Tuple items are ordered, unchangeable, 
# # and allow duplicate values.

# #Tuple items are indexed, 
# # the first item has index [0], the second 
# #item has index [1] etc.

# #Allow Duplicates
# #Since tuples are indexed, they can have 
# #items with the same value:

# thistuple = ('monday', 'thuesday', 'wednesday', 'thursday', 'monday', 'friday')
# print(thistuple)

# #Tuple Length

# #To determine how many items a tuple 
# # has, use the len() function:

# #Print the number of items in the tuple:

# thistuple = ('wednesday', 'thursday', 'friday')
# print(len(thistuple))

# #Create Tuple With One Item
# #To create a tuple with only one item, you have to add a comma after the item, otherwise Python 
# # will not recognize it as a tuple.

# #Example
# #One item tuple, remember the comma:

# thistuple = ('apple',)
# print(type(thistuple))

# #not a tuple
# thistuple = ('apple')
# print(type(thistuple))

# #Tuple Items - Data Types
# #Tuple items can be of any data type:
# #String, int and boolean data types:

# tuple1 = ('apple', 'banana', 'cherry')
# tuple2 = (1, 5, 7, 9, 3)
# tuple3 = (True, False, False)

# print(tuple1)
# print(tuple2)
# print(tuple3)

# #A tuple can contain different data types:
# #A tuple with strings, integers and boolean values:

# tuple1 = ('abc', 34, True, 40, 'male')
# print(tuple1)

# #The tuple() Constructor
# #It is also possible to use the tuple() constructor 
# #to make a tuple.

# #Using the tuple() method to make a tuple:

# thistuple = tuple(('monday', 'thuesday', 'wednesday')) #note the double round-brackets
# print(thistuple)

# #Access Tuple Items
# #You can access tuple items by referring to the 
# #index number, inside square brackets:

# #Print the second item in the tuple:

# thistuple = ('apple', 'banana', 'cherry')
# print(thistuple[1])

# #Negative Indexing
# #Negative indexing means start from the end.

# #-1 refers to the last item, -2 refers to the second last item etc.

# this_tuple = ('wednesday', 'thuesday', 'friday', 'saturday', 'sunday')
# print(this_tuple[-1])

# #Range of Indexes
# #You can specify a range of indexes by specifying where to start and where to end the range.
# #When specifying a range, the return value will be a new tuple with the specified items.
# #Return the third, fourth, and fifth item:

# this_tuple = ('monday', 'tuesday', 'friday', 'saturday', 'sunday')
# print(this_tuple[2:5])

# #By leaving out the start value, the range will start at the first item:

# #This example returns the items from the beginning to, but NOT included, "sunday":

# this_tuple = ('monday', 'tuesday', 'friday', 'saturday', 'sunday')
# print(this_tuple[:4])

# #By leaving out the end value, the range will go on to the end of the list:

# #This example returns the items from "friday" and to the end:

# this_tuple = ('monday', 'tuesday', 'friday', 'saturday', 'sunday')
# print(this_tuple[2:])

# #Range of Negative Indexes
# #Specify negative indexes if you want to start the search from the end of the tuple:
# #This example returns the items from index -4 (included) to index -1 (excluded)

# this_tuple = ('monday', 'tuesday', 'friday', 'saturday', 'sunday')
# print(this_tuple[-4:-1])

# #Check if Item Exists

# # To determine if a specified item is present in a tuple use the in keyword:

# # Example
# # Check if "sunday" is present in the tuple:

# this_tuple = ('monday', 'tuesday', 'friday', 'saturday', 'sunday')
# if "saturday" in this_tuple:
#     print("yes, saturday is in the days tuple")

    
week_days = tuple(("Monday","Thuesday","Wednesday"))
print("weekdays", week_days)


update_week_days = week_days+("Firday",)
print("update_week_days",update_week_days)











