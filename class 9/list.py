
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

std = ['minhaj',"ali","kamran"]
print(std)