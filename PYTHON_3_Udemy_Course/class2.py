from random import random


class Person:
    def __init__(self, firstname, lastname, health, status):
        """initialize atributes to be used in available for all
        class methods in this class, and for class objects created by this clas"""
        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        "All people intoduce themselves"
        print("Hello, my name is {} {}".format(self.firstname, self.lastname))

    def emot(self):
        emotion = random.randrange(1, 3)
        if emotion == 1:
            print("{} is haooy today".format(self.firstname))
        elif emotion == 2:
            print("{} is sad right now".format(self.firstname))

    def status_vhange(self):
        if self.health == 100:
            print(("{} is totally healthy!".format(self.firstname)))
        elif self.health >= 75:
            print(("{} is totally fine!".format(self.firstname)))
        elif self.health >= 50:
            print(("{} is totally unwell!".format(self.firstname)))
        else:
            print("{} is unconscious".format(self.firstname))


Maria = Person("Maria", "Gutierrez", 95, status=True)
Rey = Person("Rey", "Jones", 88, status=False)
Lee = Person("Lee", "Williams", 72, status=True)

print("{} is my friend ? {}".format(Maria.firstname, Maria.status))
print("{} is my friend ? {}".format(Rey.firstname, Rey.status))

Lee.status_vhange()


# ===========================================================================

class Enemy(Person):
    def __init__(self, weapon, firstname, lastname, health, status):
        super().__init__(firstname, lastname, health, status)
        self.weapon = weapon

    def hurt(self, other):
        if self.weapon == 'rock':
            other.health = -10
        elif self.weapon == 'stick':
            other.health -= 5
        print(other.health)

    def insult(self, other):
        if other.health <= 80:
            print("{}, you are tired and weak".format(other.firstname))
        else:
            print('You are too strong to care what anybody says about you')

    def steal(self, other):
        if other.status:
            print("ha ha ha {} I have your stuff".format(other.firstname))
        else:
            print('{}, you are a hero'. format(other.firstname))


Alex = Enemy('rock', 'Alex', 'Wayne', 75, False)
Rey = Enemy('paper', 'Rey', 'Nu', 100, True)
Alex.hurt(Maria)
Alex.insult(Rey)
Rey.steal(Alex)