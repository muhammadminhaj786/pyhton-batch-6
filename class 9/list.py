
userEmail = 'minhajwahid@gmail.com'
userPass = '1234'

# emailInp = input(' Enter email')
# passInp = input(" enter password")

def login(email,password):
    if userEmail == email and userPass == password:
        print('login successfully')
        return True
    else:
        print('invalid credentials')

# print(login(emailInp,passInp ))




#DSA
#list  ===>container for storing multiple values
std1 = 'minhaj'
std2 = 'ali'

#indexing

std = ['minhaj',"ali","kamran", "ahmed"]
print(std[0])

#add value in list   append
std.append('waqas')
print(std)

#index:length

print(std[0:3])

#update value in list
std[1] = "daniyal"

print(std)

#delete value in list   remove
std.remove('danyal')
print(std)