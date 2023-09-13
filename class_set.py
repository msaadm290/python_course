# 1. Sets are used to store multiple items in a single variable.
#A set is a collection which is unordered, unchangeable*, and unindexed.
#Set items are unchangeable, but you can remove items and add new items.
#Sets are written with curly brackets.
#Set items are unordered, unchangeable, and do not allow duplicate values.

#Unordered means that the items in a set do not have a defined order.
#Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

#Set items are unchangeable, meaning that we cannot change the items after the set has been created.

thisset = {'monday', 'thuesday', 'wednesday',}
print(thisset)

#Duplicates Not Allowed
#Sets cannot have two items with the same value.

#Duplicate values will be ignored:

thisset = {'monday', 'thuesday', 'wednesday', 'monday'}
print(thisset)

#Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
#True and 1 is considered the same value:

thisset1 = {'monday', 'tuesday', 'wednesday', True, 1, 2}

print(thisset1)






