# class BankAccount:
#     def __init__(self, owner, balance=0.0):
#         self.owner = owner
#         self.balance = balance
#
#     def get_balance(self):
#         return self.balance
#
#     def deposit(self, deposit):
#         if type(deposit) is int:
#             self.balance += deposit
#         else:
#             print('Insert correct input')
#         return f'The new deposit is {self.balance}'
#
#     def withdraw(self, withdraw):
#         if withdraw < self.balance:
#             self.balance -= withdraw
#         else:
#             print('Insufficient founds')
#         return f'The new balance is {self.balance}'
#
#
# customer1 = BankAccount('Daniel')
# print(customer1.get_balance())
# customer1.deposit(200)
# print(customer1.get_balance())
# customer1.withdraw(129)
# print(customer1.get_balance())

# ------------------------------------------------------------------
# class Chicken:
#     total_eggs = 0
#
#     @classmethod
#     def display(cls):
#         return f'There are currently {cls.total_eggs} eggs in the farm'
#
#     def __init__(self, species, name, eggs=0):
#         self.species = species
#         self.name = name
#         self.eggs = eggs
#
#     def lay_egg(self):
#         self.eggs += 1
#         Chicken.total_eggs += 1
#         return self.eggs
#
#
# c1 = Chicken(name='Alice', species='Partride Silkei')
# c2 = Chicken(name='Amelia', species='Speckled Sussex')
#
# c1.lay_egg()
# print('gaina 1 are: ', c1.eggs)
# print('Total number of eggs', Chicken.total_eggs)
#
# c1.lay_egg()
# print('gaina 1 are: ', c1.eggs)
# print('Total number of eggs', Chicken.total_eggs)
# c2.lay_egg()
# print('gaina 2 are: ', c2.eggs)
# print('Total number of eggs', Chicken.total_eggs)
# c2.lay_egg()
# print('gaina 2 are: ', c2.eggs)
# print('Total number of eggs', Chicken.total_eggs)
# c2.lay_egg()
# print('gaina 2 are: ', c2.eggs)
# print('Total number of eggs', Chicken.total_eggs)
#
# print(Chicken.display())

# ---------------------------------------------------------------------
# --------------------------INHERITANCE--------------------------------
# A key feature of OOP is the ability ti define a class which inherits fro another class ( a base or parent class)

# ------------------------PROPERTIES-------------------------








# ------------------------SUPER()---------------------------

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        

    def make_sond(self, sound):
        print(f'this animal says {sound}')

class Cat(Animal):
    pass

cat = Cat()
cat.make_sond('miau miau')