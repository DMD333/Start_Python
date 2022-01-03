# 1.Display the sum of 5 + 10, using two variables: x and y.
x = 5
y = 10
print(x+y)


# 2.Create 3 variables:
# ● One of type int  = 20.
# ● One of type float = 10.
# ● One of type string = “pytho
a = 20
b = 10.0
c = '"pytho'


# 3. Using function type check the type of :
restanta = 0
notaFinala = 10.0
laborator = "Introducere in informatica"
print(type(restanta))
print(type(notaFinala))
print(type(laborator))


# 4.  Reads two numbers and multiplies them together and print out their product.
first_number = int(input("Insert first number: "))
second_number = int(input("Insert second number: "))

print(f'The product of {first_number} * {second_number} = ', first_number * second_number)


# 5. Check if the first and last number of a string  is the same
numar = "8231230981238"
if numar[0] == numar[-1]:
    print('True')


# 6. Write a program to find how many times substring “Emma” appears in the given string.
str_x = "Emma is good developer. Emma is a writer"

print(str_x.count("Emma"))


# 7. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
exemplu = "eu merg la mare" # sa imi afiseze "eure"
print(exemplu[:2] + exemplu[-2:])


# 8. Write a Python program to calculate the length of a string.
pt = "eu merg la mare" #->15
print(len(pt))


# 9. Write a Python program to get a string from a given string where all occurrences of its first
# char have been changed to '$', except the first char itself. Go to the editor
# Expected Result : 'resta$t'
string = 'restartare'
keep_letter = string[0]
replace_letter = string.replace('r','$')
substring = keep_letter + replace_letter[1:]
print(substring)


# 10. Utilizand tipurile de print pe care vi le-am aratat:
# afisati in consola I have 1000 dollars so I can buy 3 football for 450.00 dollars.
totalMoney = 1000
quantity = 3
price = 450
print(f'I have {totalMoney} dollars so I can buy {quantity} football for {float(price)} dollars')
print('I have', totalMoney, 'dollars so I can buy', quantity, 'football for', float(price), 'dollars')


# 11. .Build a program to calculate the followings using the input from the user for a, b or r
# • rectangle area and perimeter
# • circle area
a = float(input('Insert first number: '))
b = float(input('Insert second number: '))
r = float(input('Insert radius value: '))
print('Rectangle Area is:', a * b)
print('Rectangle Perimeter is:', (a * 2) + (2 * b))
print("Circle's area is:", 3.14 * r)


# 12. Which of the following are valid ways to specify the string literal foo'bar in Python:
" Raspuns corect "   # • 'foo\'bar’
                     # • """foo'bar""”
" Raspuns corect "   # • "foo'bar"
                     # • 'foo''bar’
                     # • 'foo'bar’


# # 13.Password checker script
# # Define a username getting input from the console
# # Define a password getting input from the console
# # Display the following message ‘The password for user Paul is
# # ********* is 9 characters long)
username = input("Insert username: ")
password = input("Insert password: ")
pass_length = len(password)
star_pass_length ='*' * len(password)
print(f"The password for user {username} is {star_pass_length}", pass_length, "characters long")


# de cautat pe net:
# 14. Write a program to take three names as input from a user in the single input() function call.
for x in range(0,3):
    nume = input(f"insert nume {x+1}: ")


# 15. Display float number with 2 decimal places using print() pt num = 458.541315 afisati 458.54
num = 458.541315
print(round(num, 2))