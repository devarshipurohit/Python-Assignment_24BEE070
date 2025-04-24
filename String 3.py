# Get two strings from user
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Check substring presence
if str1 in str2 or str2 in str1:
    print("One string is a substring of the other")
else:
    print("Neither is a substring of the other")
