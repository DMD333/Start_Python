# 1.Take two int values from user and print greatest among them
a = int(input('Insert first number: '))
b = int(input('Insert second number: '))

def greatest(a, b):
    if a > b:
        result = a
    elif a == b:
        result = 'Numbers are equal'
    else: result = b
    if a == b:
        print(result)
    else:print(f'The biggest number is: {result}')
    exit()

print(greatest(a,b))

# 2.A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

# 3.A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity

# 4.Write an if statement that asks for the user's name via input() function.
# If the name is "Bond" make it print "Welcome on board 007." Otherwise make it print "Good morning NAME". (Replace Name with user's name)

# 5.Write a Python program to check the validity of password input by users.
# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

# 6.Write a Python program that tells a user that the number they entered is not a 5 or a 6.

# 7.read three numbers and writes them all in sorted order.

# 8.We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23.
# We are in trouble if the parrot is talking and the hour is before 7 or after 20.
# Return true if we are in trouble.

# 9.Given a string, return a new string where "not " has been added to the front.
# However, if the string already begins with "not", return the string unchanged.

# 10.Given a string, return true if the string starts with "hi" and false otherwise.

# 11.Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.

# 12.We'll say a number is special if it is a multiple of 11 or if it is one more than a multiple of 11.
# Return true if the given non-negative number is special.