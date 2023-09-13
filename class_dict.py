#Dictionaries are used to store data values in key:value pairs.

#A dictionary is a collection which is ordered*,
# changeable and do not allow duplicates.

#As of Python version 3.7, dictionaries are ordered. In Python 
#3.6 and earlier, dictionaries are unordered.

#Dictionaries are written with curly brackets, 
#and have keys and values:

#Dictionary items are presented in key:value pairs,
# and can be referred to by using the key name.
#Create and print a dictionary:

this_dict = {
    "brand": "toyota",
    "model": "camry",
    "year": 2006
}

print(this_dict)

this_dict1 = {
    "brand" : 'toyota',
    "model" : 'Hilander',
    "year" : 2016
}

print(this_dict1['brand'])

x = this_dict1.values()
y = this_dict.keys()
print(x)
print(y)

