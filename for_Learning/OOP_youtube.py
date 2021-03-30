# класс это шаблон создания объектов, класс это способ создания объекта


# атрибуты класса
'''
class Person:
    name = 'Ivan'
    age = 30

print(getattr(Person,'name',1000))

#изменения атрибута класса
Person.name = 'Ulian'
print(Person.name)

Person.x = 1000
setattr(Person,'money',23)
print(Person.__dict__)

del Person.x
print(Person.__dict__)

delattr(Person,'money')
print(Person.__dict__)



class Person:
    name = 'Ivan'
    age = 30

a = Person()
b = Person()

Person.z = 100


#атрибуты экземпляра класса

class Car:
    model = 'BMW'
    engine = 1.6

a1 = Car()
a2 = Car()


#функция как атрибут класса

class Car:
    model = 'BMW'
    engine = 1.6

    @staticmethod
    def drive():
        print('Lets go')

#Car.drive()
#getattr(Car,'drive')()

a = Car()
a.drive() # нельзя вызвать от экземпляра!! только от класса




class Laptop():
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = brand + ' ' + model


laptop1 = Laptop('Asus', '18-bdfx', 37000)
laptop2 = Laptop('Samsung', '13-bsdf0xx', 47000)
print(laptop1.laptop_name)


class SoccerPlayer():
    def __init__(self,name, surname):
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0

    def score(self,goals_num = 1):
        self.goals += goals_num

    def make_assist(self,assists_num = 1):
        self.assists += assists_num

    def statistics(self):
        return print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')

leo = SoccerPlayer('Leo', 'Messi')
leo.score(700)
leo.make_assist(500)
leo.statistics() # выводит "Messi Leo - голы: 700, передачи: 500"
kokorin = SoccerPlayer('Alex', 'Kokorin')
kokorin.score()
kokorin.statistics() # выводит "Kokorin Alex - голы: 1, передачи: 0"


class Zebra():
    def __init__(self,count = 0):
        self.count = count

    def which_stripe(self):
        self.count+=1
        if self.count % 2 == 0:
            print("Полоска черная")
        else:
            print("Полоска белая")

z1 = Zebra()
z1.which_stripe() # печатает "Полоска белая"
z1.which_stripe() # печатает "Полоска черная"
z1.which_stripe() # печатает "Полоска белая"


class Person():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return self.last_name + ' ' + self.first_name

    def is_adult(self):
        return self.age >= 18


p1 = Person('Jimi', 'Hendrix', 55)
print(p1.full_name())  # выводит "Hendrix Jimi"
print(p1.is_adult())  # выводит "True"


class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self,sound):
        self.sound = sound
        return f'{self.name} says {self.sound}'

jack = Dog("Jack", 4)

print(jack.description()) # распечатает 'Jack is 4 years old'
print(jack.speak("Woof Woof")) # распечатает 'Jack says Woof Woof'
print(jack.speak("Bow Wow")) # распечатает 'Jack says Bow Wow'

#моносостояние для экземпляров класса

class Cat():
    _shared_attr = {
        'breed' : 'siam',
        'color' : 'black'}
    def __init__(self):
        self.__dict__ = Cat._shared_attr

'''

#публичные,защищенные и приватные атрибуты

class BankAccount():
    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    #def print_public_data(self):
        #print(self.name,self.balance,self.passport)

    #def print_protected_data(self):
        #print(self._name,self._balance,self._passport)

    def print_private_data(self):
        print(self.__name,self.__balance,self.__passport)



account1 = BankAccount('Bob',100000,'3456qwerty')
#account1.print_protected_data()
account1.print_private_data()
print(account1.__name)
print(account1.__balance)
print(account1.__passport)