



# class veichle:

#     def __init__(self,color,serial_no):
#         self.color = color
#         self.serial = serial_no

#     def move(self):
#         print('move')
#     def welcome(self):
#         print(f"hello {self.color} {self.serial} .")

# v1 = veichle('green', '1234')
# print(v1.color)
# v1.welcome()
# pillars of opps
# inheritance

# class Dummy:
#     def test(self):
#         print('hello')


# class Car(veichle,Dummy):
#    def wheel(self):
#        print('I have 4 wheels')

# class Bike:
#     def wheel(self):
#        print('I have 2 wheels')


# car1 = Car('red','456')
# car1.welcome()
# car1.wheel()
# car1.move()
# car1.test()
# bike1 = Bike()
# bike1.wheel()

# class A:
#     def call_a(self):
#         print('A')
# a = A()
# a.call_a()

# class B(A):
#     def call_b(self):
#         print('B')
# b = B()
# b.call_b()
# b.call_a()

# class C(B):
#     def call_c(self):
#         print('C')
# c = C()
# c.call_a()
# c.call_b()
# c.call_c()


#encapsulation
class Bank:
    def __init__(self,account,balance,pin):
        self.account = account
        self.balance = balance
        self.__pin = pin


acc1 = Bank('minhaj', 450,'123')