# Please write a program which asks for the names and ages of two persons.
# The program should then print out the name of the elder.

# Some examples of expected behaviour:

# Sample output
# Person 1:
# Name: Alan
# Age: 26
# Person 2:
# Name: Ada
# Age: 27
# The elder is Ada

# Sample output
# Person 1:
# Name: Bill
# Age: 1
# Person 2:
# Name: Jean
# Age: 1
# Bill and Jean are the same age

# Write your code here:
name1 = input("Enter the first person's name: ")
age1 = int(input("Enter their age: "))

name2 = input("Enter the second person's name: ")
age2 = int(input("Enter their age: "))

if age1 > age2:
    print(name1, "is older.")
elif age2 > age1:
    print(name2, "is older.")
else:
    print("They are the same age.")
