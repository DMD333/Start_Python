# 1.Take two int values from user and print greatest among them
a = int(input('Insert first number: '))
b = int(input('Insert second number: '))


def greatest(a, b):
    if a > b:
        result = a
    elif a == b:
        result = 'Numbers are equal'
    else:
        result = b
    if a == b:
        print(result)
    print(f'The biggest number is: {result}')


print(greatest(a, b))


# 2.A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.
student_grade = int(input('Insert your score: '))


def grade():
    score = ' '
    if student_grade < 25:
        score = 'F'
    elif 25 <= student_grade < 45:
        score = 'E'
    elif 45 <= student_grade < 50:
        score = 'D'
    elif 50 <= student_grade < 60:
        score = 'C'
    elif 60 <= student_grade < 80:
        score = 'B'
    elif 80 <= student_grade:
        score = 'A'
    print(f'Your grade is: {score}')


grade()


# 3.A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
quantity = int(input('Insert quantity:'))
if quantity >= 1000:
    print("You received 10% DISCOUNT !")


# 4.Write an if statement that asks for the user's name via input() function.
# If the name is "Bond" make it print "Welcome on board 007."
# Otherwise make it print "Good morning NAME". (Replace Name with user's name)
name = input("Insert your name:")


def name_007():
    if name == 'Bond' or name == 'bond':
        print("Welcome on board 007.")
    else:
        print(f"Good morning {name}")


name_007()

# 5.Write a Python program to check the validity of password input by users.
# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

import re
regex = re.compile('[`~!@#$%^&*(){}=+_/\|?.,><":;]')
password = input("Insert PASSWORD:")
length_pass = len(password)


def chek_password():
    if length_pass < 6 or length_pass > 16:
        print("Verify the length of your PASSWORD !")
    elif not any(c.islower() for c in password):
        print('Must add LOWER case character')
    elif not any(x.isupper() for x in password):
        print('Must add UPPER case character')
    elif regex.search(password) is None:
        print('PASSWORD must contain special character')
    elif not any(a.isdigit() for a in password):
        print('PASSWORD must contain numeric characters !')
    else:
        print('You are all set !')


print(chek_password())


# 6.Write a Python program that tells a user that the number they entered is not a 5 or a 6.
number = int(input('insert number: '))


def chek_number():
    if 5 != number != 6:
        print(f'The number {number} is not number 5 neither 6')
    else:
        print('You entered number', number)


chek_number()


# 7.read three numbers and writes them all in sorted order.
numbers = []
for x in range(3):
    read = int(input(f'Insert number {x+1}: '))
    numbers.append(read)
    numbers.sort()
print(numbers)


# 8.We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23.
# We are in trouble if the parrot is talking and the hour is before 7 or after 20.
# Return true if we are in trouble.
def loud_parrot():
    hour = int(input('Insert hour: '))
    if 7 > hour or hour > 20:
        print(True, ' We are in trouble')
    else:
        print(False, ' We are not in trouble')

loud_parrot()


# 9.Given a string, return a new string where "not " has been added to the front.
# However, if the string already begins with "not", return the string unchanged
def add_not():
    string = input('Insert name: ')
    if 'not' in string[:3]:
        print(string)
    else:
        string = 'not ' + string
        print(string)

add_not().



# 10.Given a string, return true if the string starts with "hi" and false otherwise.
def hello():
    insert = input('Insert string: ')
    if 'hi' in insert[0:2]:
        print(True)
    else:
        print(False)

hello()


# 11.Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.
def sum():
    a = int(input('insert 1st number: '))
    b = int(input('insert 2nd number: '))
    adunare = a + b
    if 10 <= adunare <= 19:
        print('Sum is', 20)
    else:
        print(f'Suma este = {adunare}')

sum()


# 12.We'll say a number is special if it is a multiple of 11 or if it is one more than a multiple of 11.
# Return true if the given non-negative number is special.

def special():
    insert = int(input("Insert number: "))
    if insert / 11 == 0 or insert - 11 =
