# variables and data types
# numbers
# a = 4
# b = 6

# # arithmetic operations
# print("the sum of a and b is :", a + b)
# print("the difference of and b is :", a-b)
# print("the product of a and b is :", a*b)
# print("the division of a and b is :", a/b)
# print("the floor division of a and b is :", a//b)
# print("the modulus of a and b is :", a % b)
# print("the exponent of a and b is :", a**b)


# # area of circle
# PI = 3.14
# r = 5
# area = PI * r*r
# print("the area of circle os :", area)

# # strings
# name = "ibrahim"
# age = 18
# email = "ibra@gmail.com"
# is_student = False
# print(f"my name is  {name} and my age is {age} and this is my email {email}")
# print(f"i'm a student: {is_student}");

# # control flow
# # if-else
# num =10
# if num >12:
#     print(f" {num} is grater than 12")
# elif num ==12:
#     print(f"{num} is equal to 12")
# else:
#     print(f"{num} is less than 12")

# if age >= 18:
#     print("you are eligible to vote")
# elif age == 17:
#     print("you will be eligible to vote next year")
# elif age == 16:
#     print("you will be eligible to vote in two years")
# else:
#     print("you are not eligible to vote")


# # truthy and falsy values
# if "hello":
#     print("this is  runs  value")


# if "":
#     print("this  won't run  value")

# if 0:
#     print("this  won't value")

# if 4:
#     print ( " this will runs value")

# if []:
#     print("this won't run")


# items = [6]
# if items:
#     print("lis is not empty")
# else:
#     print("list is empty")

# if my_list := []:  # Using the walrus operator to assign and check in one line
#     print("list is not empty")

# # loops

# my_name = "ibrahim";
# for letter in my_name:
#     print(f"the letter is : {letter}")

# print("**********")

# print(f"\n the length of my name is : {len(my_name)}")
# # array
# fruits = ["apple", "banaana", "cherry", "mango"]
# print(fruits[1])

# # list
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in numbers:
#     print(f"the number is : {number}")
# print(numbers[5])

#  break and continue
# print out 1,2,3,4

count =0 
# while True:
#     print(count)
#     count += 1
#     if count >= 5:
#         break

while count < 5.132:
    print(count)
    count +=1
else:
    print("count value reached %f" %(count));


#  print only add numbers
for x in range(10):
    # check if x is add
    if x %2 == 0:
        continue
    print(f"this is and add number: {x}")


print("\n*************")
#  print only even numbers

for e in range(10):
    if e % 2 != 0:
        continue
    print(f"this is an even numbers: {e}")

for i in range(1,10):
    if(i%5==0):
        continue
    print(f"this is a value of i: {i}")
else:
    print("this is not printed because the loop is terminatedbecause of break but not due to fail in condition")


numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

for number in numbers:
    if number == 237:
        break
    if number % 2 == 1:
        continue
    print(number)




