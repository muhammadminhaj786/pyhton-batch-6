# modular
#first method
# import mymodule 
# print(mymodule.add(5,5))


#second method
 # from mymodule import add
# print(add(5,5))


#third method
# # import mymodule as z
# print(z.add(4,7))



#exception try 



# def myApp():
#     num = int(input("Enter a number: "))
#     if num == 0:
#         print('"Zero not allowed')
#         return
#     print(10/num)

# myApp()

# try:
#     num = int(input("Enter a number: "))
#     print(10/num)
# except ZeroDivisionError:
#     print("zero is not divisible")
# except ValueError:
#     print('num is not divsible by string')
# finally:
#     print('bye')

# print('sab shi he ')

import math_utils as mu
print(mu.mul(4,5))

import numpy as np
print(np.__version__)

arr = np.array([1,2,3])
print(type(arr))