# 1. Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
# Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of the rectangle.
# Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.
# Create a Parallelepiped child class inheriting from the Rectangle class and with a height attribute and another Volume() method to calculate the volume of the Parallelepiped
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        perimeter = 2 * self.length + 2 * self.width
        print(perimeter)

    def area(self):
        area = self.length * self.width
        print(area)

    def display(self):
        print(f'lungimea este: {self.length}')
        print(f'latimea este: {self.width}')
        print('Perimetrul este'), self.perimeter()
        print(f'Aria este:'), self.area()


class Parallelepiped(Rectangle):
    def __init__(self, height, length, width):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        vol = self.height * self.length * self.width
        print(f'Volumul paralelipipedului este: {vol}')


# 2. Define a Book class with the following attributes: Title, Author (Full name), Price.
# Set the View() method to display information for the current book.
class Book:
    def __init__(self, title, author_full_name, price):
        self.title = title
        self.author_full_name = author_full_name
        self.price = price

    def view(self):
        print(f'The Book {self.title} written by author: {self.author_full_name} costs {self.price}')


# 3. Create a Python class Person with attributes: name and age of type string.
# Create a display() method that displays the name and age of an object created via the Person class.
# Create a child class Student  which inherits from the Person class and which also has a section attribute.
# Create a method displayStudent() that displays the name, age and section of an object created via the Student class.
# Create a student object via an instantiation on the Student class and then test the displayStudent method.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f'{self.name} have {self.age} years')


class Student(Person):
    def __init__(self, section, name, age):
        self.section = section
        super().__init__(name, age)

    def displayStudent(self):
        print(f'{self.name} have {self.age} years and it\'s enrolled at {self.section}')


# 4.Create a Python class called BankAccount which represents a bank account, having as
# attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
# Create a constructor with parameters: accountNumber, name, balance.
# Create a Deposit() method which manages the deposit actions.
# Create a Withdrawal() method  which manages withdrawals actions.
# Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
# Create a display() method to display account details.
class BanckAccount:
    def __init__(self, accountNumber, name, balance=0):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def deposit(self, deposit):
        self.balance += deposit
        print(f'Your current balance is: {self.balance}$')

    def withdraw(self, withdraw):
        if withdraw > self.balance:
            print('Not enough founds !')
        else:
            self.balance -= withdraw
            print(f'Your current balance is: {self.balance}$')

    def bankFees(self):
        fees = self.balance * 0.05
        print(f'For {self.balance}$ Bank charge you with {fees}$')

    def display(self):
        print(f'Account Owner:{self.name} \nAccount Number: {self.accountNumber} \nCurrent Balance: {self.balance}$')


# 5
# Create a Coputation class with a default constructor (without parameters) allowing to perform various calculations on integers numbers.
# Create a method called Factorial() which allows to calculate the factorial of an integer. Test the method by instantiating the class.
# Create a method called Sum() allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. Test this method.
# Create a method called testPrim() in  the Calculation class to test the primality of a given integer. Test this method.
# Create  a method called testPrims() allowing to test if two numbers are prime between them.
# Create a tableMult() method which creates and displays the multiplication table of a given integer.
# Then create an allTablesMult() method to display all the integer multiplication tables 1, 2, 3, ..., 9.
# Create a static listDiv() method that gets all the divisors of a given integer on new list called  Ldiv.
# Create another listDivPrim() method that gets all the prime divisors of a given integer.
class Computation:
    def __init__(self):
        self.nr = 6

    def factorial(self):
        number = 1
        for x in range(1, self.nr):
            number *= x
        print(number)

    def sum(self):
        number = 0
        for x in range(1, self.nr):
            number += x
        print(number)

    def testPrim(self, nr1, nr2):
        if nr1 % 2 != 0 and nr1 % 3 != 0:
            print(f'{nr1} --> is prime number')
        else:
            print(f'{nr1} --> NOT prime')

        if nr2 % 2 != 0 and nr2 % 3 != 0:
            print(f'{nr2} --> is prime number')
        else:
            print(f'{nr2} --> NOT prime')
        max_number = max(nr1, nr2)
        min_number = min(nr1, nr2)
        if max_number % min_number != 0:
            print(f'{nr1} and {nr2} are prime between them')
        else:
            print(f'{nr1} and {nr2} are not prime')


# #1
# lengts = Rectangle(10, 2)
# lengts.display()
# vol = Parallelepiped(5, 10, 2)
# vol.volume()

# #2
# book = Book('Scrisoare de dragoste', 'Mihail Drumes', price=30.99)
# book.view()

# #3
# student = Student('QA Automation', 'Daniel', age='30')
# student.display()
# student.displayStudent()

# #4
# owner = BanckAccount(190078, 'Daniel Dumitru', 200)
# owner.withdraw(470)
# owner.withdraw(50)
# print(owner.balance)
# owner.deposit(27)
# owner.bankFees()
# owner.display()

# 5
numar = Computation()
numar.factorial()
numar.sum()
numar.testPrim(17, 191)
