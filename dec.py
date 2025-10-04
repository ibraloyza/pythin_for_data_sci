#  understandig Dictionary in python  as data science
# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
# Dictionaries are used to store data values like a map, which, unlike other Data Types that hold only a single value as an element, can hold multiple values.
# Dictionaries are one of the most commonly used data structures in Python.
# Dictionaries are mutable, meaning that you can change their content without changing their identity.
# Dictionaries can contain items of different data types, including other dictionaries.
# Dictionaries are indexed, meaning that you can access individual items in a dictionary using their key.
# Dictionaries can be iterated, meaning that you can loop through the items in a dictionary using a for loop.
# how to create a dictionary in python and how does it work
my_info = {
    "id": 101,
    "name": "ibrahim",
    "age": 25,
    "email": "ibra@gmail.com",
    "is_student": True,
    "courses": ["python","JavaScript","Django"],
    "address": {
        "street": "30 fagax St",
        "city": "mogadishu",
        "country": "somalia"
    }
}

# print(f"the dictionary items in the my_info dictionary is : {my_info}");
# print(f"this is my address : {my_info['address']}");

#  looping through a dictionary using a for loop to print specific key and value
# for key,value in my_info.items():
#     print(f"this is my address {key} : {value}")
for key , value in my_info.items():
    print(f"this is my address  {key} {value}:{my_info[key]} {my_info['address']}");

square = {x: x**2 for x in range(10)}
print(f"the square of numbers from 0 to 9 is : {square}");

#  exercise 🟢 Beginner Level (Basics of Dictionary)
# 1 Create a dictionary called student with keys: "name", "age", and "grade".Assign any values you want.

student = {
    "name ": "ibrahim",
    "age": 25,
    "grade": "A"
}

#2. Print only the "name" from the dictionary.
print(f"the name of  the student is : {student['name ']}")

# 3. Add a new key "country" with any value you want.
student["country"] = "somalia"
print(f"the updated student dictionary is : {student}")

#4. Change the student’s "grade" to "A+".
student["grade"] = "A+"
print(f"the updated grade of the student is : {student}")

#5.  Delete the "age" key.
del student["age"];
print(student)

# 6. Loop through all the keys and values, printing them like: name: Ali, grade: A+, etc
for key, value in student.items():
    print(key+" : "+value);

# 7. Use .get() to safely get a key that doesn’t exist (like "email") and print what it returns.
print(student.get('email', "Email not found"));


#8.  exercie 🟡 Intermediate Level (Thinking with Dictionaries)

#  You have this dictionary:
prices = {
    "apple": 2,
    "banaana" : 1,
    "orange": 3
}

# Add "mango": 4
prices["mango"] = 4;
# Update the price of "apple" to 2.5
print(f"before updating apple price is :{prices}")
prices["apple"] = 2.5;

# Print all fruits that cost more than 2.

print(prices);

# 9. Create a dictionary of 3 people where each key is their name and the value is their age.
people = {
    "ali" :20,
    "amina": 22,
    "ibrahim":25,
}
# Find and print the oldest person’s name.
get_all_ages = people.values();
print(get_all_ages);
print(f"the aldest person is  : {max(people.values())}");

# Combine two dictionaries: 

a = {
    "x":1,
    "y": 2
}

b = {
    "z": 3
}
# The modern way (Python 3.9+):
compined = a | b;
print (compined);

# The update method (works in older versions too):
copy_a  = a.copy();
copy_a.update(b);
print(copy_a)
# The dictionary unpacking trick:

unpacking = {**a , **b}
print(unpacking);









 