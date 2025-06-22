#loop for loop

 # for a 

# num = 13
# x = 23
# print("a" or "p"  in "apple")
# print( x > 20 and x <9)

# for a in range(1,11):
#     print('hello', a)



#function

# print("hello")
# print("hello")
# print("hello")
# print("hello")
# print("hello")
# print("hello")
# print("hello")
# print("hello")
# print("hello")
# print("hello")


# for a in range(10):
#     print('hello')

#ya function blue light red light ko on kar wai ga
# def greeting(a):
#     print("hello", a)

# greeting("minhaj")

# def=>keyword funcation_name(parameter):
#     block of code
# call_function(argument)

# def sum(a,b):
#     return a+ b
#     # c = a + b
# print(sum(10,20))


a = int(input('Enter first number'))
b = int(input('Enter second number'))
# c = int(input('Enter third number'))


def max(a,b,c=8):
    if a > b and a > c:
        return a
    elif b> a and b >c :
        return b
    else:
        return c
print(max(a,b))


