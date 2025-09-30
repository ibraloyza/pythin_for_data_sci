# learning list in  python as a data structure
# A list is a collection of items that are ordered and changeable. In Python, lists are written with square brackets.
# Lists are used to store multiple items in a single variable.
# Lists are one of the most commonly used data structures in Python.
# Lists are mutable, meaning that you can change their content without changing their identity.
# Lists can contain items of different data types, including other lists.
# Lists are indexed, meaning that you can access individual items in a list using their index.
# Lists can be sliced, meaning that you can access a range of items in a list using their index.
# Lists can be iterated, meaning that you can loop through the items in a list using a for loop.
# Here is an example of a list in Python:
fruits =  ["apple","banaana", "cherry", "mango","orange" ];
print(f"the list items in the fruits list is : {fruits}");
# Here is an example of accessing individual items in a list using their index:
print(f"this is the first iten in the fruits list is : {fruits[0]}");
print(f"this is the last item in the lis is : {fruits[-1]}");
# Here is an example of slicing a list using their index:
print(f"the items from index 1 to 3 in  the fruits list is : {fruits[1:4]}");
# Here is an example of changing the content of a list:
fruits[1]= "kiwi";
print(f"the changed list items in the fruits list is : {fruits}");
# here is an example of adding an item to a list using the append() method:
fruits.append("grape");
print(f"the list items in the fruits list after appending is : {fruits}");
# here is an example of removing an item from a list using the remove() method:
fruits.remove("kiwi");
print(f"the list items in the fruits list after removing is : {fruits}");
# here is an example of inserting an item to a list using the insert() method:
fruits.insert(1,"kiwi");
print(f"the list items in the fruits list after inserting is : {fruits}");

# here is an example of looping through the items in a list using a for loop:
for fruit in fruits:
    print(f"the fruit in the list is : {fruit}");
# here is an example of checking if an item is in a list using the in keyword:
if "apple" in fruits:
    print("yes, apple is in the fruits list");
else:
    print("no, apple is not in the fruits list");

# here is an example of finding the length of a list using the len() method:
print(f"the length of the fruits list is : {len(fruits)}");
# here is an example of sorting a list using the sort() method:
fruits.sort();
print(f"the sorted list items in the fruits list is : {fruits}");
# here is an example of reversing a list using the reverse() method:
fruits.reverse();
print(f"the reversed list items in the fruits list is : {fruits}");
# here is an example of copying a list using the copy() method:
fruits_copy = fruits.copy();
print(f"the copied list items in the fruits_copy list is : {fruits_copy}");

# here is an example of clearing a list using the clear() method:
fruits.clear();
print(f"the cleared list items in the fruits list is : {fruits}");
# here is an example of creating a list using the list() constructor:
numbers = list((1,2,3,4,5,6,7,8,9,10));
print(f"the list items in the numbers list is : {numbers}");
# here is an example of finding the index of an item in a list using the index() method:
print(f"the index of 5 in the numbers list is : {numbers.index(5)}");
