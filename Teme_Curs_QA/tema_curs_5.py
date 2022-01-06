# 1) return the number of 9's in a list
a = [1, 2, 9]  # → 1
b = [1, 9, 9]  # → 2
c = [1, 9, 9, 3, 9]  # → 3


def find_9(arr_1, arr_2, arr_3):
    count_1 = 0
    count_2 = 0
    count_3 = 0
    for x in arr_1:
        if x == 9:
            count_1 += 1
    print(f'We found number 9 {count_1} times')
    for x in arr_2:
        if x == 9:
            count_2 += 1
    print(f'We found number 9 {count_2} times')
    for x in arr_3:
        if x == 9:
            count_3 += 1
    print(f'We found number 9 {count_3} times')


find_9(a, b, c)

# -------------------- OR 2nd version which is easier --------------------------

w = a.count(9)
y = b.count(9)
z = c.count(9)
print(f'We fount 9 {w} times')
print(f'We fount 9 {y} times')
print(f'We fount 9 {z} times')


# 2) Write a Python program that prints all the numbers from 0 to 6 except 3 and 6
def no_print_3_and_6():
    for x in range(0, 7):
        if x != 3 and x != 6:
            print(x)


no_print_3_and_6()


# 3) Print sum of the numbers between 20 and 100
def sum_20_to_100():
    suma = 0
    for x in range(20, 101):
        suma += x
    print(suma)


sum_20_to_100()

# 4) Write a Python program which iterates the integers from 1 to 50.
# For multiples of 3 print "Fizz" instead of the number and for the multiples of 5 print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
def fizz_buzz():
    for x in range(1, 51):
        if (x > 3 and x % 3 == 0) and (x > 5 and x % 5 == 0):
            print(f'FizzBuzz for number {x}')
        elif (x > 3 and x % 3 == 0):
            print(f'Fizz for number {x}')
        elif x > 5 and x % 5 == 0:
            print(f'Buzz for number {x}')
        else:
            print(x)


fizz_buzz()


# 5) Write a Python program to create the multiplication table (from 1 to 10) of a number.
# Input a number: 6
def multiplication_table():
    number = int(input('Insert number: '))
    for x in range(1, 11):
        print(f'{number} X {x} = ', number * x)


multiplication_table()

# 6) Write a Python program to construct the following pattern
# Expected Output:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999
def pattern():
    patt = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for x in range(10):
        print(patt[x - 1] * x)


pattern()
# ---------------------------- OR -----------------------------------
def pattern_2():
    patt_2 = range(1, 10)
    for x in patt_2:
        print(f'{x}' * x)

pattern_2()

# 7) Write a program to print n natural number in descending order
def descending_natural_number():
    insert_1 = int(input('Insert first number: '))
    insert_2 = int(input('Insert second number: '))
    if insert_1 < insert_2:
        numar = range(insert_1, insert_2 + 1)
    else:
        numar = range(insert_2, insert_1 + 1)
    array = []
    count = 0
    for x in numar:
        array.append(x)
    print(array[::-1])

descending_natural_number()


# 8) Print max and minim from the list

def max_min():
    lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
    min = lst[0]
    max = lst[0]
    for x in lst:
        if x <= min:
            min = x
        elif x >= max:
            max = x
    print('This is maximum', max)
    print('This is minimum', min)


max_min()


# 9) Count how many times 6 occur in the list.
# Using .remove() method, clear the last element of the list.
def find_6():
    lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
    counting = lst.count(6)
    print(f'We found 6 in list {counting} times')
    lst.remove(lst[-1])
    print(lst)

find_6()


# 10) Concatenate two lists in the following order
list1 = ["Hello ", ", take", " a sit"]
list2 = ["Dear", "Sir"]

print(list1[0] + list2[0] + ' ' + list2[1] + list1[1] + list1[2])
print(list1 + list2)

# 11) Add the
sub_list = ["socks", "tshirt", "pajamas"] #to the end of the gift_list
gift_list = ['socks', '4K drone', 'wine', 'jam']
gift_list.append(sub_list)
print(gift_list)

# 12) Given 2D array calculate the sum of diagonal elements.
def diagonala_sum():
    exemplu = [[1, 3, 5],[1, 4, 6],[7, 6, 9]]
    counting = len(exemplu)
    sum = 0
    for x in range(counting):
        for y in range(counting):
            if x == y:
                sum += exemplu[x][y]
    print(sum)


diagonala_sum()

# 13) Add item 7000 after 6000 in the following Python List
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
def insert_number():
    insert = int(input('Insert number: '))
    # list1.append([2][2]insert)


# 14) Given a Python list, find value 20 in the list, and if it is present, replace it with 200.
#  Only update the first occurrence of a value
def replace_element():
    list1 = [5, 10, 15, 20, 25, 50, 20]
    counting = 0

    for x in list1:
        counting += 1
        if x == 20:
            list1[counting - 1] = 200
            break
    print(list1)

replace_element()


# 17) Remove empty strings from the list of strings
def remove_empty():
    new_string = ["Mike", "", "Emma", "Kelly", "", "Brad"]
    for x in new_string:
        if x == "":
            new_string.remove(x)
    print(new_string)


remove_empty()


# 18) Write a program that appends the square of each number to a new list. (o noua lista cu patratul fiecarui element)
def square():
    insert = int(input('Insert number: '))
    answer = True
    arr = []

    while answer:
        want_to_continue = input('Do you want to continue : ( Y / N ): ')
        if want_to_continue == 'Y' or want_to_continue == 'y':
            arr = arr + [insert]
            insert = int(input('Insert another number: '))
            print(f'You added {insert} to the list')
        else:
            arr = arr + [insert]
            print('Your list is: ', arr)
            answer = False
            break
square()


# 19) Write a function that takes a list as a parameter and returns the reversed list. Do NOT use the built-in reverse() function.
def reverse_list():
    first_list = [2, 17, 18, 91, 177, 31, 87, 202, 44, 30]
    new_list = []
    counting = 0
    length = len(first_list)

    for x in range(length):
        counting += 1
        new_list.append(first_list[length - counting])
    print(new_list)

reverse_list()



# 20) Write a python program to print the first 10 numbers Fibonacci series
def fibonaci():
    x = 0
    y = 1
    counting = 0

    while counting < 10:
        sir_fibonaci = x + y
        x = y
        y = sir_fibonaci
        counting += 1
        print(f'{counting})', sir_fibonaci)

fibonaci()

# 21) Write a python program to read a number and print a right triangle using "*"
# Input : 5
# ----------Output---------
# *
# * *
# * * *
# * * * *
# * * * * *

def stars():
    number = int(input('Insert number: '))
    for x in range(number):
        print('* ' * (x + 1))

stars()

# 22) Write a python program to check given number is prime or not
def prime_number(number):
    verifica = type(number)
    if verifica is int:
        print(f'Number {number} is a prime number')
    else:
        print(f'{number} is not prime')
    exit()

print(prime_number(-11))

# 23) Write a python program to print all prime numbers between 0 to 100 , and print how many prime numbers are there.
def prime_1_to_99():
    counting = 0
    for x in range(1, 100):
        counting += 1
        print('-->', x)
    print(f'There are counted {counting} numbers')


prime_1_to_99()