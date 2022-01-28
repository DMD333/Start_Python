ion = ['ion neculaie', 30, 'IT', 2002]
vasile = ['Vasilica neculaie', 25, 'Marketing', 2020]


# -----------------------------------------------------------------
class Muncitor:
    def __init__(self, nume, age, section):
        self.nume = nume
        self.age = age
        self.section = section

    def super_angajat(self):
        if self.age > 10:
            print(self.nume + ' este super angajat')
        else:
            print(self.nume + ' nu merita bonus')


angajat1 = Muncitor('Vasile Caraiman', 30, 'Marketing')
# print(angajat1.nume)

angajat2 = Muncitor('Costel Gigel', 49, 'Marketing')
# print(angajat2.section)
#
# if(angajat1.age > angajat2.age):
#     print((f'{angajat1.nume} are {angajat1.age}'))
# else:
#     print(f'{angajat2.nume} are {angajat2.age}')

angajat1.super_angajat()


# --------------------------------------------------------------
class Dog:
    def __init__(self, name, age, rasa):
        self.name = name
        self.age = age
        self.rasa = rasa

    def cumFace(self, actiune):
        print(f'{self.name} stie sa faca {actiune}')

    def canMakePuppies(self, hasPedigree):
        if hasPedigree == True:
            print(f'{self.name} can make puppies')


spark = Dog('spark', 4, 'Labrador')
marley = Dog('marley', 8, 'Huskey')

# marley.cumFace('wof wof')
# spark.canMakePuppies(True)


# ---------------------------------------------------------------
# MOSTENIREA tuturor funtiilor din clasa DOG

class Labrador(Dog):
    def __init__(self, munca, name, age, rasa):
        super().__init__(name, age, rasa)
        self.munca = munca

    def ceStie(self, actiune='wof wof wof wof'):
        self.cumFace(actiune)
        # print(f'{self.name} ' + actiune)


benji = Labrador('Politist', 'Benji', 5, 'Labrador')
# benji.ceStie()
# print(benji.name)
benji.ceStie()
