# understand tuples in python as a data structure
# A tuple is a collection of items that are ordered and unchangeable. In Python, tuples are written with round brackets.
# Tuples are used to store multiple items in a single variable.
# Tuples are one of the most commonly used data structures in Python.
# Tuples are immutable, meaning that you cannot change their content without changing their identity.
# Tuples can contain items of different data types, including other tuples.
# Tuples are indexed, meaning that you can access individual items in a tuple using their index.
# Tuples can be sliced, meaning that you can access a range of items in a tuple using their index.
# Tuples can be iterated, meaning that you can loop through the items in a tuple using a for loop.
#  how to create a tuple in python and how does it work
# Here is an example of a tuple in Python:
fruits =  ("apple","banaana", "cherry", "mango","orange" );
print(f"the tuple items in the fruits tuple is : {fruits}");

# what is the difference between a list and a tuple in python
# the main difference between a list and a tuple is that a list is mutable, meaning that you can change its content without changing its identity, while a tuple is immutable, meaning that you cannot change its content without changing its identity.
# Here is an example of accessing individual items in a tuple using their index:
print(f"this is the first iten in the fruits tuple is : {fruits[3]}");
# here is an example of  methods in the tuples

print(f"the length of the fruits tuple is : {len(fruits)}");
print(f"the maximum item in the fruits tuple is : {max(fruits)}");
print(f"the minimum item in the fruits tuple is : {min(fruits)}");
print(f"the count of the item 'apple' in the fruits tuple is : {fruits.count('apple')}");
print(f"the index of the item 'cherry' in the fruits tuple is : {fruits.index('cherry')}");
# here is an example of slicing a tuple
print(f"the items from index 1 to 3 in the fruits tuple is : {fruits[1:4]}");
# here is an example of iterating through a tuple
for fruit in fruits:
    print(f"the item in the fruits tuple is : {fruit}");
# here is an example of nested tuples
nested_tuple = (fruits, (1, 2, 3), ("a", "b", "c"));
print(f"the nested tuple is : {nested_tuple}");
print(f"the first item in the nested tuple is : {nested_tuple[0]}");
print(f"the second item in the nested tuple is : {nested_tuple[1]}");
print(f"the third item in the nested tuple is : {nested_tuple[2]}");
print(f"the first item in the first item of the nested tuple is : {nested_tuple[0][0]}");
print(f"the second item in the second item of the nested tuple is : {nested_tuple[1][1]}");
# here is an example of tuple unpacking
(a, b, c, d, e) = fruits
print(f"the first item in the unpacked tuple is : {a}");
print(f"the second item in the unpacked tuple is : {b}");
print(f"the third item in the unpacked tuple is : {c}");
# here is an example of using the tuple() constructor to create a tuple
my_tuple = tuple(("apple", "banana", "cherry")) # note the double round brackets
print(f"the tuple created using the tuple() constructor is : {my_tuple}");
# here is an example of converting a list to a tuple
my_list = ["apple", "banana", "cherry"]
my_tuple_from_list = tuple(my_list)
print(f"the tuple created from a list is : {my_tuple_from_list}");
# here is an example of converting a string to a tuple
my_string = "hello"
my_tuple_from_string = tuple(my_string)
print(f"the tuple created from a string is : {my_tuple_from_string}");