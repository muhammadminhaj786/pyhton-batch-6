



class Animal:

    def __init__(self,name):
        self.name = name
    def can_eat():
        print('yes')

    def can_walk(self): 
        print('yes')

    def speak(self):
        pass
    def can_speak(ask):
        print(ask)

class Dog(Animal):
    def can_bite(self):
        print('yes bite')
    def speak(self):
        print('bark')


class Cat(Dog):
    def speak(self):
        print('meow')


# animal1 = Animal()
dog1 = Dog('puppy')
dog1.speak()
# dog1 = Dog()
# dog1.can_walk()
cat1 = Cat('kitty')
cat1.speak()


class Bank:
    def __init__(self, account, balance, pin):
        self.account = account
        self.balance = balance
        self.__pin = pin
    def pin_show(self):
        print(self.__pin)


account1 = Bank('minhaj', 4500, '123')
account1.pin_show()


class Shape:
    def area(self):
        pass

