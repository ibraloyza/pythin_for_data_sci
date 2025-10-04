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
# Create a dictionary called student with keys: "name", "age", and "grade".Assign any values you want.

student = {
    "name ": "ibrahim",
    "age": 25,
    "grade": "A"
}

# Print only the "name" from the dictionary.
print(f"the name of  the student is : {student['name ']}")

# Add a new key "country" with any value you want.
student["country"] = "somalia"
print(f"the updated student dictionary is : {student}")

# Change the student’s "grade" to "A+".
student["grade"] = "A+"
print(f"the updated grade of the student is : {student}")

# Delete the "age" key.
del student["age"];
print(student)

# Loop through all the keys and values, printing them like: name: Ali, grade: A+, etc
for key, value in student.items():
    print(key+" : "+value);

# Use .get() to safely get a key that doesn’t exist (like "email") and print what it returns.
print(student.get('email', "Email not found"));


