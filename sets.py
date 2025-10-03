#  understanding of sets. This module provides a simple implementation of a set data structure
# A set is a collection of items that are unordered, unchangeable, and unindexed. In Python, sets are written with curly brackets.
# Sets are used to store multiple items in a single variable.
# Sets are one of the most commonly used data structures in Python.
# Sets are mutable, meaning that you can change their content without changing their identity.
# Sets can contain items of different data types, including other sets.
# Sets are not indexed, meaning that you cannot access individual items in a set using their index
# Sets can be iterated, meaning that you can loop through the items in a set using a for loop.
# how to create a set in python and how does it work
# Here is an example of a set in Python:
fruits =  {"apple","banana", "cherry", "mango","orange" };
print(f"the set items in the fruits set is : {fruits}");
# what is the difference between a list and a set in python
# the main difference between a list and a set is that a list is ordered and indexed, meaning that you can access individual items in a list using their index, while a set is unordered and unindexed, meaning that you cannot access individual items in a set using their index.
# Here is an example of iterating through a set
for fruit in fruits:
    print(f"the item in the fruits set is : {fruit}");
# here is an example of  methods in the sets
print(f"the length of the fruits set is : {len(fruits)}");
fruits.add("kiwi")
print(f"the set after adding 'kiwi' is : {fruits}");
fruits.remove("banana")
print(f"the set after removing 'banana' is : {fruits}");
# fruits.remove("cambo") # this will raise a KeyError because 'cambo' is not in the set
# print(f"the set after trying to remove 'cambo' is : {fruits}");
fruits.discard("cambo") # this will not raise an error because 'cambo' is not in the set
print(f"the set after trying to discard 'cambo' is : {fruits}");
# discard() method does not raise an error if the item to be removed is not found in the set
print(f"before popping a random item the set is : {fruits}");
fruits.pop()  # removes a random item from the set
print(f"the set after popping a random item is : {fruits}");

fruits.clear() # removes all items from the set
print(f"the set after clearing all items is : {fruits}");

# here is an example of using the set() constructor to create a set
my_set = set(("apple", "banana", "cherry")) # note the double round brackets
print(f"the set created using the set() constructor is : {my_set}");

# here is an example of converting a list to a set
my_list = ["apple", "banana", "cherry"]
my_set_from_list = set(my_list)
print(f"the set created from a list is : {my_set_from_list}");
