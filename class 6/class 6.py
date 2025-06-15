
#atm
print('hello')
# correct 
# if (conditon):

#     print(valid)
# else:
#     print(not valid)

#pin,current amount, required amount,slip


# 1)pin defined
# 2)Enter a pin
# 3) check valid pin
# 3)current amount defined
# 4)enter required amount
# checkoutn amount
# 5)genrate slip
# 6)not genrate slip


pin = '1234'
currentAmount = 5000
user_pin = input('Enter a pin')
if user_pin == pin:
    print('valid')
    required_amount = int( input('Enter amount'))

    if current_amount >= required_amount:
        print('possible')
        current_amount =current_amount - required_amount
        print(current_amount)
        user_slip = input('do you want to generate slip yes/no')
        if user_slip == 'yes':
            print('Generate slip', current_amount)
        else: 
            print('not generated', current_amount)

    else:
        print('not possible')
else:
    print('not valid')

# 