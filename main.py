import string
import random
#collect user details
def get_details():
    first_name = (input('Enter your first name: '))
    last_name = (input('Enter your last name: '))
    user_email = (input('Enter your Email address: '))
    #listing user details
    details = [first_name,last_name,user_email]

    return details

#generate random password using user first and last name
def gen_password(details):
    #using string import
    characters = string.ascii_letters
    length = 5
    #importing the random module
    random_password = ''.join([random.choice(characters) for n in range(length)])
    password = str(details[0][0:2] + details[1][-2:] + random_password)
    return password

status = True
container = []

while status:
    #get user details
    details = get_details()

    # to see password generated
    password = gen_password(details)
    print('Your password is: ' + str(password))

    #find out if the users wants to continue
    password_like = input(str('Accept generated password? If YES, enter YES else enter your new password'))

    password_loop = True

    while password_loop:
        if password_like == 'yes':
            #add password to user details
            details.append(password)

            #to add user details to overall container
            container.append(details)

            password_loop = false;

        else:
            #enter user password >=
            user_password = input(str('Enter password longer than or equal to 7'))

            #password length
            password_length = True

            while password_length:
                if len(user_password) >= 7:
                    #add password to detail
                    details.append(user_password)
                    container.append(details)

                    #break out of loop
                    password_length = False
                    password_loop = False
                else:
                    print('Your password is less than 7')
                    user_password = input(str('Enter password longer than or equal to 7'))

        new_user = input(str('Would you like to enter a new user? '))

        if (new_user == 'No'):

            status = False
            for item in container:
                print(item)
            else:
                status = True
        break
