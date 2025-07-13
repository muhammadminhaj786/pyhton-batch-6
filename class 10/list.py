
# userEmail = 'minhajwahid@gmail.com'
# userPass = '1234'

# # emailInp = input(' Enter email')
# # passInp = input(" enter password")

# def login(email,password):
#     if userEmail == email and userPass == password:
#         print('login successfully')
#         return True
#     else:
#         print('invalid credentials')

# # print(login(emailInp,passInp ))




# #DSA
# #list  ===>container for storing multiple values
# std1 = 'minhaj'
# std2 = 'ali'

# #indexing

# std = ['minhaj',"ali","kamran", "ahmed"]
# print(std[0])

# #add value in list   append
# std.append('waqas')
# print(std)

# #index:length

# print(std[0:3])

# #update value in list
# std[1] = "daniyal"

# print(std)

# #delete value in list   remove
# std.remove('danyal')
# print(std)



stds = ["a","b","c","d"]

# for std in stds:
#     print(std)


# nums = [1,2,3,4,5,6,7,8,9,10]
# even = []
# odd = []


# def arrangeNum(nums):
   
#    for num in nums:
#      if num %2== 0:
#         even.append(num)
#      else: 
#         odd.append(num)
# return even
   

# arrangeNum(nums)

# stds = ["a","b","c"]

# if "c" in stds:
#     stds.remove("c")
    
# print(stds)


#dictionary
std1 = {
    "name": "ali",
    "rollNo": "123",
    "phoneNumber": "123"
}

std1["name"] = "usama"
# std1["city"] = "karachi"
# std1.pop("rollNo")
# std1.get("name")
print(std1["name"])

# for key, value in std1.items():
#     print( value)

std = [{
    "name": "ali",
    "rollNo": 123,
    "active": True,
},{ "name": "usama",
    "rollNo": "123",
    "active": True,},{ "name": "imran",
    "rollNo": "123",
    "active": True,}]

print(std)