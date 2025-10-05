#  understandig Dictionary in python  as data science
# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
# Dictionaries are used to store data values like a map, which, unlike other Data Types that hold only a single value as an element, can hold multiple values.
# Dictionaries are one of the most commonly used data structures in Python.
# Dictionaries are mutable, meaning that you can change their content without changing their identity.
# Dictionaries can contain items of different data types, including other dictionaries.
# Dictionaries are indexed, meaning that you can access individual items in a dictionary using their key.
# Dictionaries can be iterated, meaning that you can loop through the items in a dictionary using a for loop.
# how to create a dictionary in python and how does it work
# my_info = {
#     "id": 101,
#     "name": "ibrahim",
#     "age": 25,
#     "email": "ibra@gmail.com",
#     "is_student": True,
#     "courses": ["python","JavaScript","Django"],
#     "address": {
#         "street": "30 fagax St",
#         "city": "mogadishu",
#         "country": "somalia"
#     }
# }

# print(f"the dictionary items in the my_info dictionary is : {my_info}");
# print(f"this is my address : {my_info['address']}");

#  looping through a dictionary using a for loop to print specific key and value
# for key,value in my_info.items():
#     print(f"this is my address {key} : {value}")
# for key , value in my_info.items():
#     print(f"this is my address  {key} {value}:{my_info[key]} {my_info['address']}");

# square = {x: x**2 for x in range(10)}
# print(f"the square of numbers from 0 to 9 is : {square}");

#  exercise 🟢 Beginner Level (Basics of Dictionary)
# 1 Create a dictionary called student with keys: "name", "age", and "grade".Assign any values you want.

# student = {
#     "name ": "ibrahim",
#     "age": 25,
#     "grade": "A"
# }

#2. Print only the "name" from the dictionary.
# print(f"the name of  the student is : {student['name ']}")

# 3. Add a new key "country" with any value you want.
# student["country"] = "somalia"
# print(f"the updated student dictionary is : {student}")

#4. Change the student’s "grade" to "A+".
# student["grade"] = "A+"
# print(f"the updated grade of the student is : {student}")

#5.  Delete the "age" key.
# del student["age"];
# print(student)

# 6. Loop through all the keys and values, printing them like: name: Ali, grade: A+, etc
# for key, value in student.items():
#     print(key+" : "+value);

# 7. Use .get() to safely get a key that doesn’t exist (like "email") and print what it returns.
# print(student.get('email', "Email not found"));


#8.  exercie 🟡 Intermediate Level (Thinking with Dictionaries)

#  You have this dictionary:
# prices = {
#     "apple": 2,
#     "banaana" : 1,
#     "orange": 3
# }

# Add "mango": 4
# prices["mango"] = 4;
# Update the price of "apple" to 2.5
# print(f"before updating apple price is :{prices}")
# prices["apple"] = 2.5;

# Print all fruits that cost more than 2.

# print(prices);

# 9. Create a dictionary of 3 people where each key is their name and the value is their age.
# people = {
#     "ali" :20,
#     "amina": 22,
#     "ibrahim":25,
# }
# Find and print the oldest person’s name.
# get_all_ages = people.values();
# print(get_all_ages);
# print(f"the aldest person is  : {max(people.values())}");

#10 . Combine two dictionaries: 

# a = {
#     "x":1,
#     "y": 2
# }

# b = {
#     "z": 3
# }
# The modern way (Python 3.9+):
# compined = a | b;
# print (compined);

# The update method (works in older versions too):
# copy_a  = a.copy();
# copy_a.update(b);
# print(copy_a)
# The dictionary unpacking trick:

# unpacking = {**a , **b}
# print(unpacking);

# 11. Count the number of vowels in the word "dictionary" using a dictionary where keys are vowel letters and values are counts.

# vowels = {
#     "a":0,
#     "e":0,
#     "i":0,
#     "o":0,
#     "u":0
# }
# word = "dictionary";
# for letter in word:
#     if letter in vowels:
#         vowels[letter]=+1;
#         print(letter);


# 🔵 Advanced Level (Real Thinking)
# 12. You have a nested dictionary:
students = {
    "s1":{"name":"ibrahim","marks":100},
    "s2":{"name":"farah","marks":99},
    "s3":{"name":"ahmed","marks":100}
}

highest_marks = 0
top_student = ""

for key , value in students.items():
    if value['marks'] > highest_marks:
        highest_marks = value["marks"];
        top_student = value['name'];
print(f"top student is : {top_student} and his marks is : {highest_marks}");


# 13. Use a dictionary comprehension to create:

squares = {1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81,10:100};

new_squares = {key: value + 15 for (key,value) in squares.items()}
print(new_squares);

keys = ["a","b","c","d","e"];
values =[1,2,3,4,5];

myDic =  {k:v for (k,v)in zip(keys,values)};
print(myDic);

dic = dict.fromkeys(range(10),True);
print(dic);


sentence = "I love python because I love coding"

words = sentence.split();
print(words);

word_count = {}

# Loop through each word
for word in words:
    # Increase count if word exists, otherwise start at 1
    word_count[word] = word_count.get(word, 0) + 1

# Print the result
print("Word frequency:", word_count)

# for word in words:
#     if word in word_count:
#         word_count[word] =+1;
#     else:
#         word_count[word] = 1;

# print(f"this is word count :{word_count}");

scores = {"Ali": 88, "Amina": 99, "Khadar": 77}
sorted_dict = dict( sorted(scores.items(), key=lambda x: x[1]))

print(sorted_dict);

text = "hello world";

ch_count = {};

for ch in text:
    ch_count[ch] = ch_count.get(ch,0) + 1;

print(ch_count);




    










 