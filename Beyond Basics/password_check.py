correct_password = "Python123"
name = input('Enter your name: ')
password = input('Enter your password: ')

while correct_password != password:
    password = input('Sorry not recognised, try again: ')

loginMessage = "Hi %s you have successfully logged in" % name

print(loginMessage)
