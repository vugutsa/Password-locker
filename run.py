#!/usr/bin/env python3.6
from user import User
from credentials import Credentials

def create_user(user_name,password):
    '''
    Function to create a new user
    '''
    new_user = User(user_name,password)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()
    
def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()
    
def find_user(user_name):
    '''
    Function that finds a user by number and returns the user
    '''
    return User.find_by_user_name(user_name)

def check_existing_users(user_name):
    '''
    Function that check if a user exists with that number and return a Boolean
    '''
    return User.user_exist(user_name)

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()



def create_credentials(user_name1,password,handle):
    '''
    Function to create a new credentials
    '''
    new_credentials = Credentials(user_name1,password,handle)
    return new_credentials

def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()
    
def del_credentials(credentials):
    '''
    Function to delete a credentials
    '''
    credentials.delete_credentials()
    
def find_credentials(user_name1):
    '''
    Function that finds a credentials by user_name and returns the credentials
    '''
    return Credentials.find_by_user_name1(user_name1)

def check_existing_credentials(user_name1):
    '''
    Function that check if a credentials exists with that number and return a Boolean
    '''
    return Credentials.credentials_exist(user_name1)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()



def main():
    print("Hello! PLease insert your username!")
    print( "Welcome to the Password-locker. Apply these commands to continue:CH = create handle," )
    short_code = input().lower()
    if short_code == 'ch':
        print('Enter new handle details')
        print('*' * 100)
        handle = input('Enter handleName: ')
        username = input('Enter Username: ')
        while True:
            print('use :  EP =  enter password')
            password_choice = input().lower()
            if password_choice == 'ep':
                password = input('Enter Password: ')
                break
            else:
                print('Invalid short code. Please try again')
            save_user(create_user(username, password))
        print('*' * 100)
        print(f'Welcome {username} to your new handle your password is <--- {password} --->')
        print('*' * 100)
    while True:
        print('Use these short codes to manage credentials: \n NC = new credential, \n VC = display credentials,\n SC =     find credential  \n Dc = delete credential, \n  EX = exit application')
        short_code = input().lower()
        if short_code == 'nc':
            print('Enter New Credential Details')
            print('*' * 100)
            handle = input('Handle Name : ')
            user_name1 = input('Username : ')
            while True:
                print('Use: EP = enter password?')
                password_choice = input().lower()
                if password_choice == 'ep':
                    password = input('Enter password : ')
                    break
                else:
                    print('Invalid short code. Please try again')
                print('*' * 100)
            save_credentials(create_credentials(handle, user_name1,password))
            print('*' * 100)
            print(f'Your {handle} handle has been saved')
            print('*' * 100)
        elif short_code == 'vc':
            if display_credentials():
                print('Your saved credentials are:')
                for handle in display_credentials():
                    print('*' * 100)
                    print(f' Name: {handle} \n Username: {user_name1} \n Password: {password}')
                    print('*' * 100)
            else:
                print('*' * 100)
                print('You have No Credentials. Please Create One')
                print('*' * 100)
        elif short_code == 'dc':
            print('Enter Handle name to delete...')
            name = input('Handle Name : ')
            print('*' * 100)
            if find_credentials(user_name1):
                name_result = find_credentials(user_name1)
                name_result.delete_credentials()
                print(f'Handle {name} has been successfully deleted ')
                print('*' * 100)
            else:
                print('Incorrect handle name')
                print('*' * 100)
        elif short_code == 'sc':
            print('Enter Handle Name To Search...')
            search = input('Handle Name : ')
            print('*' * 100)
            if find_credentials(search):
                search = find_credentials(search)
                print(f'Handle Name: {search} ')
                print('*' * 100)
            else:
                print('Credentials does not exist')
                print('*' * 100)
        elif short_code == 'ex':
            print('Goodbye')
            print('*' * 100)
            break
        else:
            print('Invalid Short code. Please try again!')
            print('*' * 100)
if __name__ == '__main__':
    main()

def main():
    print("Hello! PLease insert your username!")
    print('Welcome to the Password-locker. Apply these commands to continue: CH = create handle,' )
    short_code = input().lower()
    if short_code == 'ch':
        print('Enter new handle details')
        print('*' * 100)
        username = input('Enter Username: ')
        while True:
            print('use :  EP = to manually enter your own password')
            password_choice = input().lower()
            if password_choice == 'ep':
                password = input('Enter Password: ')
                break
            else:
                print('Invalid short code. Please try again')
            save_user(create_user(user_name, password))
        print('*' * 100)
        print(f'Welcome {username} to your new handle your password is <--- {password} --->')
        print('*' * 100)
    while True:
        print('Use these short codes to manage credentials: \n NC = new credential, \n VC = display credentials,\n SC =     find credential  \n Dc = delete credential, \n  EX = exit application')
        short_code = input().lower()
        if short_code == 'nc':
            print('Enter New Credentials Details')
            print('*' * 100)
            handle = input('Handle Name : ')
            user_name1 = input('Username : ')
            while True:
                print('Use: EP = manually enter password?')
                password_choice = input().lower()
                if password_choice == 'ep':
                    password = input('Enter password : ')
                    break
                else:
                    print('Invalid short code. Please try again')
                print('*' * 100)
            save_credentials(create_credentials(handle, user_name1,password))
            print('*' * 100)
            print(f'Your {handle} handle has been saved')
            print('*' * 100)
        elif short_code == 'vc':
            if display_credentials():
                print('Your saved credentials are:')
                for handle in display_credentials():
                    print('*' * 100)
                    print(f' Name: {handle} \n Username: {user_name1} \n Password: {password}')
                    print('*' * 100)
            else:
                print('*' * 100)
                print('You have No Credentials. Please Create One')
                print('*' * 100)
        elif short_code == 'dc':
            print('Enter Handle name to delete...')
            name = input('Handle Name : ')
            print('*' * 100)
            if find_credentials(name):
                name_result = find_credentials(user_name1)
                name_result.delete_credentials()
                print(f'Handle {name} has been successfully deleted ')
                print('*' * 100)
            else:
                print('Incorrect handle name')
                print('*' * 100)
        elif short_code == 'sc':
            print('Enter Handle Name To Search...')
            search = input('Handle Name : ')
            print('*' * 100)
            if find_credentials(search):
                search = find_credentials(search)
                print(f'Handle Name: {search} ')
                print('*' * 100)
            else:
                print('Credentials does not exist')
                print('*' * 100)
        elif short_code == 'ex':
            print('Goodbye')
            print('*' * 100)
            break
        else:
            print('Invalid Short code. Please try again!')
            print('*' * 100)
            
if __name__ == '__main__':
    main()