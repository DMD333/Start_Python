# se citesc 4 valori de la tastatura ( a b c d)
# daca c + d > 0 se afiseaza a+b
# daca c+d = 0 se afiseaza a-b
# daca c+d <0 se adiseaza a*b

a = int(input('Inset number: '))
b = int(input('Inset number: '))
c = int(input('Inset number: '))
d = int(input('Inset number: '))

if c + d > 0:
    print("Suma este =", a + b)
elif c + d == 0:
    print("Suma este =", a - b)
else:
    print("Suma este =", a * b)

# 5. Write a Java program that keeps a number from the user and generates an integer between 1 and 7 and displays the name of the weekday
insert = int(input("Insert number: "))
weekdays = ['Luni', 'Marti', 'Miercuri', 'Joi', 'Vineri', 'Sambata', 'Duminica']

if 1 >= insert or insert <= 7:
    print(f'Ziua saptamanii este {weekdays[insert - 1]}')
else:
    print("Wrong number")


# Write a Python script that takes input from the user and displays that input back in upper and lower cases.
cuv = input('Cuvant: ')
nume_revers = cuv[::-1]
nume_upper = cuv.upper()
print(nume_upper, nume_revers)

# Write a Python function to get a string made of its first three characters of a specified string.
# If the length of the string is less than 3 then return the original string

def get_string(sir):
    if len(sir) < 3:
        return sir
    else:
        return sir[0:3]

print(get_string("Da"))

myList = [2, 18, 12 , 19, 434]
print( 19 in myList)

def sum_of_list():
    list = [2, 3, 4, 5, 6, 7, 8, 9]
    sum = 0
    for x in list:
        sum += x
    print(sum)

sum_of_list()


# 9.Given a string, return a new string where "not " has been added to the front.
# However, if the string already begins with "not", return the string unchanged.

def dd_not():
    array = []

    for x in range(3):
        name = input('Insert name: ')
        array.append(name)
        if 'not' in array[x][0:3]:
            print('Mame already contain "Not"')
        else:
            array[x] = 'not ' + array[x]
    print(array)

dd_not()
